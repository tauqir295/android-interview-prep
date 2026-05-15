---
hide:
  - toc
---

## Boot Init and System Server Deep Dive

## Overview

Android boot is a staged trust and initialization pipeline from bootloader,
kernel, and init to framework service readiness.

## Boot sequence

- bootloader verifies and loads kernel/ramdisk
- kernel initializes core subsystems
- init parses rc scripts, mounts filesystems, launches daemons
- zygote starts and forks system_server
- system_server starts core framework services
- launcher starts when readiness gates pass

## system_server role

system_server hosts critical services such as:

- ActivityManagerService
- PackageManagerService
- WindowManagerService
- PowerManagerService

Crashes or deadlocks here affect the whole device UX.

## init rc reliability and security

Init scripts define service ordering and privilege boundaries. Risk areas:

- incorrect service dependencies
- wrong SELinux context/permissions
- restart loops hiding root cause

## Watchdog mechanisms

Watchdog monitors critical threads and service responsiveness. On timeout,
Android captures diagnostics and may restart affected processes.

## Interview guidance

Strong answers cover both startup performance and failure handling quality,
including diagnostics and rollback discipline.
