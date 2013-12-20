# -*- coding: utf-8 -*-

import re
import json
import requests
from datetime import datetime


class Song(object):
    def __init__(self, artist=None, title=None, description=None,
                 composer=None, conductor=None, **kwargs):
        self.artist = artist.encode('utf-8')
        self.title = title.encode('utf-8')
        self.description = description.encode('utf-8')
        self.composer = composer.encode('utf-8')
        self.conductor = conductor.encode('utf-8')

    def __repr__(self):
        return 'Song(%s - %s)' % (self.artist, self.title)


class Episode(object):
    def __init__(self, title=None, starttimeutc=None,
                 endtimeutc=None, **kwargs):
        self.title = title.encode('utf-8')
        self.starttimeutc = starttimeutc
        self.endtimeutc = endtimeutc

    def __repr__(self):
        return 'Episode(%s)' % self.title

    @staticmethod
    def json_to_datetime(date):
        match = re.match('/Date\((\d+)\)/', date)
        if not match:
            return None
        return datetime.fromtimestamp(int(match.group(1)) / 1000.0)

    @property
    def starttime(self):
        return self.json_to_datetime(self.starttimeutc)

    @property
    def endtime(self):
        return self.json_to_datetime(self.endtimeutc)


class Playlist(object):
    def __init__(self, now=None, next=None, content=Song):
        self.now = content(**now) if now else None
        self.next = content(**next) if next else None

    def __repr__(self):
        return 'Playlist(%s, %s)' % (self.now, self.next)


class Channel(object):
    def __init__(self, name=None, id=None, siteurl=None, color=None,
                 image=None, url=None, **kwargs):
        if not id:
            raise Exception('No such channel')

        self.id = id
        self.name = name.encode('utf-8')
        self.siteurl = siteurl
        self.color = color
        self.image = image
        self.url = url

    def __repr__(self):
        return 'Channel(%s)' % self.name

    @property
    def song(self):
        payload = dict(channelid=self.id)
        response = SverigesRadio.call('/playlists/rightnow', payload)
        if not response:
            return Playlist()

        playlist = response.get('playlist')
        if not playlist:
            return Playlist()

        song = playlist.get('song')
        nextsong = playlist.get('nextsong')

        return Playlist(now=song, next=nextsong)

    @property
    def program(self):
        payload = dict(channelid=self.id)
        response = SverigesRadio.call('/scheduledepisodes/rightnow', payload)
        if not response:
            return Playlist()

        channel = response.get('channel')
        if not channel:
            return Playlist()

        currentepisode = channel.get('currentscheduledepisode')
        nextepisode = channel.get('nextscheduledepisode')

        return Playlist(now=currentepisode, next=nextepisode, content=Episode)


class SverigesRadio(object):
    @classmethod
    def call(cls, method, payload={}):
        url = 'http://api.sr.se/api/v2/%s' % method

        payload['format'] = 'json'

        response = requests.get(url, params=payload)
        if response.status_code != 200:
            return {}

        return json.loads(response.text)

    @classmethod
    def channels(cls):
        payload = dict(size=500)
        data = cls.call('/channels', payload)
        channels = data.get('channels')
        return [Channel(**channel) for channel in channels]

    @classmethod
    def channel(cls, id):
        data = cls.call('/channels/%s' % id)
        return Channel(**data.get('channel', {}))

    @classmethod
    def schedule(cls, channelid=None, programid=None):
        payload = dict(size=500, channelid=channelid, programid=programid)
        data = cls.call('/scheduledepisodes', payload)
        if not data:
            return []
        schedule = data.get('schedule')
        return [Episode(**episode) for episode in schedule]
