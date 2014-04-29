# -*- coding: utf-8 -*-
# CoAuthor Robert Tomkowski <robert.tomkowski@laboratorium.ee>
from __future__ import unicode_literals

from datetime import datetime

from django.utils.translation import pgettext, ugettext as _, ungettext


def date(time, accuracy=None):

    accuracy_types = ['seconds', 'hours', 'days', 'weeks', 'months', 'years']

    if accuracy and accuracy not in accuracy_types:
        raise ValueError(
            '{} is not valid accuracy type, valid values are: {}'.format(accuracy, ', '.join(accuracy_types))
        )

    now = datetime.now(time.tzinfo)

    if time > now:
        past = False
        diff = time - now
    else:
        past = True
        diff = now - time

    seconds = int(diff.total_seconds())

    if seconds < 10:
        return _('just now')
    if seconds < 60 or accuracy == 'seconds':
        return _pretty_format(seconds, ungettext('second', 'seconds', seconds), past)
    minutes = seconds / 60
    if minutes < 2:
        return past and _('a minute ago') or _('in a minute')
    if minutes < 60 or accuracy == 'minutes':
        return _pretty_format(minutes, ungettext('minute', 'minutes', minutes), past)
    hours = minutes / 60
    if hours < 2:
        return past and _('an hour ago') or _('in an hour')
    if hours < 24 or accuracy == 'hours':
        return _pretty_format(hours, ungettext('hour', 'hours', hours), past)
    days = hours / 24
    if days < 2:
        return past and _('yesterday') or _('tomorrow')
    if days < 7 or accuracy == 'days':
        return _pretty_format(days, ungettext('day', 'days', days), past)
    weeks = days / 7
    if weeks < 2:
        return past and _('last week') or _('next week')
    if days < 31 or accuracy == 'weeks':
        return _pretty_format(weeks, ungettext('week', 'weeks', weeks), past)
    months = days / 31
    if months < 2:
        return past and _('last month') or _('next month')
    if days < 365 or accuracy == 'months':
        return _pretty_format(months, ungettext('month', 'months', months), past)
    years = days / 365
    if years < 2:
        return past and _('last year') or _('next year')
    return _pretty_format(years, ungettext('year', 'years', years), past)


def _pretty_format(amount, text, past):
    if past:
        base = pgettext(
            'Moment in the past',
            "%(amount)d %(quantity)s ago"
        )
    else:
        base = pgettext(
            'Moment in the future',
            "in %(amount)d %(quantity)s"
        )
    return base % dict(amount=amount, quantity=text)
