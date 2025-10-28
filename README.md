# janusbot

Architecture (Simplified)

+------------------------+
| Telegram Bot (aiogram) |
+------------------------+
            |
            | commands / status / notifications
            v
+-------------------------------+
| Market Making Core            |
| * Connecting to MEXC, BitMart |
| * Quotes / orders             |
| * Spread control              |
+-------------------------------+
            |
            | queue of messages / events 
            v
+--------------------+
| Notifier / Monitor |
+--------------------+