# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Pollen charm business logic."""

import glob
import os
import subprocess
from pathlib import Path

from charms.operator_libs_linux.v0 import apt
from charms.operator_libs_linux.v1 import systemd
from charms.operator_libs_linux.v2 import snap

from exceptions import ConfigurationWriteError, InstallError


class PollenService:
    """Pollen service class."""

    @classmethod
    def prepare(cls) -> None:
        """Install packages and write configuration files.

        Raises:
            InstallError: if the packages fail to install
            ConfigurationWriteError: something went wrong writing the configuration
        """
        try:
            apt.update()
            apt.add_package(["pollinate", "ent"])
            snap.add("gtrkiller-pollen", channel="candidate")
        except FileNotFoundError as exc:
            raise InstallError from exc
        try:
            subprocess.run(
                [
                    "rsync",
                    "files/logrotate.conf",
                    "/etc/logrotate.d/pollen",
                ],
                check=True,
            )
            subprocess.run(
                [
                    "rsync",
                    "files/rsyslog.conf",
                    "/etc/rsyslog.d/40-pollen.conf",
                ],
                check=True,
            )
            systemd.service_restart("rsyslog.service")
        except FileNotFoundError as exc:
            raise ConfigurationWriteError from exc
        except systemd.SystemdError as exc:
            raise ConfigurationWriteError from exc
        if glob.glob("/dev/tpm*") or Path("/dev/hwrng").exists():
            try:
                apt.add_package("rng-tools5")
                cls.check_rng_file()
                systemd.service_restart("rngd.service")
            except FileNotFoundError as exc:
                raise ConfigurationWriteError from exc

    @classmethod
    def start(cls):
        """Start the pollen service."""
        cache = snap.SnapCache()
        pollen = cache["gtrkiller-pollen"]
        pollen.start()

    @classmethod
    def stop(cls):
        """Stop the pollen service."""
        cache = snap.SnapCache()
        pollen = cache["gtrkiller-pollen"]
        pollen.stop()

    @classmethod
    def check_rng_file(cls):
        """Check if the rng-tools-debian file needs modification."""
        file_modified = False
        with open("/etc/default/rng-tools-debian", "r", encoding="utf-8") as file:
            if file.read().count('RNGDOPTIONS="--fill-watermark=90% --feed-interval=1"') > 1:
                file_modified = True
        if not file_modified:
            with open("/etc/default/rng-tools-debian", "a", encoding="utf-8") as file:
                file.writelines(['RNGDOPTIONS="--fill-watermark=90% --feed-interval=1"'])
