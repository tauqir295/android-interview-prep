---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/networking/">← Back to Networking</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/networking/${hash}`);
      return;
    }

    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {
    // Keep default generated page link if URL parsing fails.
  }
})();
</script>

## WebSockets & Streaming Deep Dive

## Overview
WebSockets enable real-time bidirectional communication.
## Core Concepts
- Full-duplex (both directions simultaneously)
- Persistent connection
- Low latency vs polling
## Code Examples
```kotlin
// OkHttp WebSocket
val webSocket = httpClient.newWebSocket(
    Request.Builder().url("wss://echo.websocket.org").build(),
    object : WebSocketListener() {
        override fun onMessage(s: WebSocket, text: String) {
            println("Received: $text")
        }
        override fun onFailure(w: WebSocket, t: Throwable, r: Response?) {
            t.printStackTrace()
        }
    }
)
webSocket.send("Hello")
```
## Senior-Level Insights
- Reconnection logic essential
- Heartbeat/ping-pong for keep-alive
- Handle graceful disconnect
