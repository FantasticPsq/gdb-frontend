# -*- coding: utf-8 -*-
#
# gdb-frontend is a easy, flexible and extensionable gui debugger
#
# https://github.com/rohanrhu/gdb-frontend
# https://oguzhaneroglu.com/projects/gdb-frontend/
#
# Licensed under GNU/GPLv3
# Copyright (C) 2019, Oğuzhan Eroğlu (https://oguzhaneroglu.com/) <rohanrhu2@gmail.com>

import api.url

urls = api.url.URLS({
    "main": {
        "url": "/",
        "match": "^/$",
        "module": "url_modules.main.main"
    },
    "api-state": {
        "url": "/api/state",
        "match": "^/api/state$",
        "module": "url_modules.api.state"
    },
    "api-state-get": {
        "url": "/api/state/{info}",
        "match": "^/api/state/(.+)$",
        "module": "url_modules.api.state"
    },
    "api-shell": {
        "url": "/api/shell",
        "match": "^/api/shell$",
        "module": "url_modules.api.shell"
    },
    "api-event": {
        "url": "/api/event",
        "match": "^/api/event$",
        "module": "url_modules.api.event"
    },
    "api-fs-list": {
        "url": "/api/fs/list",
        "match": "^/api/fs/list$",
        "module": "url_modules.api.fs.list"
    },
    "api-fs-read": {
        "url": "/api/fs/read",
        "match": "^/api/fs/read$",
        "module": "url_modules.api.fs.read"
    },
    "api-fs-write": {
        "url": "/api/fs/write",
        "match": "^/api/fs/write$",
        "module": "url_modules.api.fs.write"
    },
    "api-sources": {
        "url": "/api/sources$",
        "match": "^/api/sources$",
        "module": "url_modules.api.sources"
    },
    "api-registers": {
        "url": "/registers$",
        "match": "^/registers$",
        "module": "url_modules.api.registers"
    },
    "api-breakpoint-add": {
        "url": "/breakpoint",
        "match": "^/api/breakpoint/add$",
        "module": "url_modules.api.breakpoint.add"
    },
    "api-breakpoint-del": {
        "url": "/breakpoint/delete",
        "match": "^/api/breakpoint/del$",
        "module": "url_modules.api.breakpoint.del"
    },
    "api-breakpoint-set-enabled": {
        "url": "/api/breakpoint/set_enabled",
        "match": "^/api/breakpoint/set_enabled$",
        "module": "url_modules.api.breakpoint.set_enabled"
    },
    "api-breakpoint-set-condition": {
        "url": "/api/breakpoint/set_condition",
        "match": "^/api/breakpoint/set_condition$",
        "module": "url_modules.api.breakpoint.set_condition"
    },
    "api-runtime-signal": {
        "url": "/api/runtime/signal",
        "match": "^/api/runtime/signal",
        "module": "url_modules.api.runtime.signal"
    },
    "api-runtime-terminate": {
        "url": "/debug/terminate",
        "match": "^/debug/terminate",
        "module": "url_modules.api.runtime.terminate"
    },
    "api-runtime-attach": {
        "url": "/api/runtime/attach",
        "match": "^/api/runtime/attach$",
        "module": "url_modules.api.runtime.attach"
    },
    "api-runtime-run": {
        "url": "/debug/run",
        "match": "^/debug/run$",
        "module": "url_modules.api.runtime.run"
    },
    "api-runtime-pause": {
        "url": "/debug/pause",
        "match": "^/debug/pause$",
        "module": "url_modules.api.runtime.pause"
    },
    "api-runtime-step": {
        "url": "/debug/step",
        "match": "^/debug/step$",
        "module": "url_modules.api.runtime.step"
    },
    "api-runtime-next": {
        "url": "/debug/next",
        "match": "^/debug/next$",
        "module": "url_modules.api.runtime.next"
    },
    "api-runtime-stepi": {
        "url": "/api/runtime/stepi",
        "match": "^/api/runtime/stepi$",
        "module": "url_modules.api.runtime.stepi"
    },
    "api-runtime-continue": {
        "url": "/debug/continue",
        "match": "^/debug/continue$",
        "module": "url_modules.api.runtime.continue"
    },
    "api-thread-switch": {
        "url": "/api/thread/switch",
        "match": "^/api/thread/switch$",
        "module": "url_modules.api.thread.switch"
    },
    "api-stack-trace": {
        "url": "/debug/stack/trace",
        "match": "^/debug/stack/trace$",
        "module": "url_modules.api.stack.trace"
    },
    "api-stack-switch": {
        "url": "/api/stack/switch",
        "match": "^/api/stack/switch$",
        "module": "url_modules.api.stack.switch"
    },
    "api-frame-variable": {
        "url": "/debug/watches",
        "match": "^/debug/watches$",
        "module": "url_modules.api.frame.variable"
    },
    "api-variables": {
        "url":"/debug/variables",
        "match":"^/debug/variables",
        "module":"url_modules.api.frame.variables"
    },
    "api-load": {
        "url": "/api/load",
        "match": "^/api/load$",
        "module": "url_modules.api.load"
    },
    "api-connect": {
        "url": "/api/connect",
        "match": "^/api/connect$",
        "module": "url_modules.api.connect"
    },
    "api-disassemble": {
        "url": "/api/disassemble",
        "match": "^/api/disassemble$",
        "module": "url_modules.api.disassemble"
    },
    "api-disassemble-frame": {
        "url": "/api/disassemble-frame",
        "match": "^/api/disassemble-frame$",
        "module": "url_modules.api.disassemble_frame"
    },
    "api-switch-theme": {
        "url": "/api/switch-theme",
        "match": "^/api/switch-theme$",
        "module": "url_modules.api.switch_theme"
    },
    "api-enhanced-collabration-enable": {
        "url": "/api/collabration/enhanced-collabration-enable",
        "match": "^/api/collabration/enhanced-collabration-enable$",
        "module": "url_modules.api.collabration.enhanced_collabration_enable"
    },
    "api-enhanced-collabration-disable": {
        "url": "/api/collabration/enhanced-collabration-disable",
        "match": "^/api/collabration/enhanced-collabration-disable$",
        "module": "url_modules.api.collabration.enhanced_collabration_disable"
    },
    "api-process-all": {
        "url": "/api/process/all",
        "match": "^/api/process/all$",
        "module": "url_modules.api.process.all"
    },
    "api-process-sigkill": {
        "url": "/api/process/sigkill",
        "match": "^/api/process/sigkill$",
        "module": "url_modules.api.process.sigkill"
    },
    "api-process-sigterm": {
        "url": "/api/process/sigterm",
        "match": "^/api/process/sigterm$",
        "module": "url_modules.api.process.sigterm"
    },
    "main-layout": {
        "url": "/{layout}/",
        "match": "^/(.+?)/?$",
        "module": "url_modules.main.main",
        "force_slash": True
    }
})