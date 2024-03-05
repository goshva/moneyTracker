#!/usr/bin/bash
/usr/bin/git -C /var/www/bots/moneyTracker/ pull && /var/www/bots/moneyTracker/git-auto -o -p && /usr/bin/git -C /var/www/bots/moneyTracker push
