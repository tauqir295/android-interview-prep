---
hide:
  - toc
---

## Security SELinux and Sandboxing Deep Dive

## Overview

Android security is layered: app sandboxing, permission checks, Binder identity,
and SELinux mandatory access control.

## Core layers

- Linux UID/GID app isolation
- framework permission and AppOps checks
- Binder caller identity enforcement
- SELinux domain/type policy constraints

## SELinux practical model

SELinux policies define which domains may access which object types with what
operations. This limits blast radius even after app-level logic bugs.

## Debugging denials safely

- gather AVC denial logs
- verify labels and domain transitions first
- add minimal allow rules only when justified
- keep release builds enforcing, not permissive

## Privilege escalation patterns

Common issues:

- missing caller validation in binder entry points
- confused deputy flows
- unsafe exported components forwarding untrusted data

Mitigation requires explicit identity checks and strict input validation.

## Runtime permission mapping

Permissions are policy-state in framework and enforced at API boundaries,
while kernel/SELinux provide deeper capability enforcement.

## Interview guidance

Good answers show layered thinking and avoid one-control narratives such as
"permissions alone solve security".
