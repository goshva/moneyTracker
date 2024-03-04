#!/usr/bin/bash
cd /var/www/bots/moneyTracker
/usr/bin/git -C /var/www/bots/moneyTracker/ pull && ./git-auto -o -p && /usr/bin/git -C /var/www/bots/moneyTracker push
