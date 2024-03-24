###
# Copyright (c) 2024, Dorian Harmans
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

from bs4 import BeautifulSoup

from supybot import utils, plugins, ircutils, callbacks, world, conf, log
from supybot.commands import *
from supybot.i18n import PluginInternationalization

try:
    from supybot.i18n import PluginInternationalization

    _ = PluginInternationalization("WorldTime")
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

HEADERS = {
    "User-agent": "Mozilla/5.0 (compatible; Supybot/Limnoria %s; KNMI plugin)" % conf.version
}

class KNMI(callbacks.Plugin):
    """A plugin to grab the daily weather prediction from the KNMI (Koninklijk Nederlands Meteorologisch Instituut), the meteorological institute of The Netherlands."""
    threaded = True

    def _init__(self, irc):
        super().__init__(irc)
        
        self._last_channel = None

    def die(self):
        super().die()

    def w1(self, irc, msg, args):
        """
        KNMI Weerbericht 1
        """
        self._last_channel = msg.channel

        url = "https://www.knmi.nl/nederland-nu/weer/verwachtingen"
        page = utils.web.getUrl(url, headers=HEADERS).decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        text_x1 = soup.select_one('.weather__text > p:nth-child(2)').text
        text_y1 = BeautifulSoup(text_x1, 'html.parser').getText()
        text_z1a = text_y1.replace("\xa0", " ")
        text_z1b = text_z1a.replace("Vanochtend", "\x02Vanochtend\x02")
        text_z1c = text_z1b.replace("Vanmiddag", "\x02Vanmiddag\x02")
        text_z1d = text_z1c.replace("Vanavond", "\x02Vanavond\x02")
        s = '(1) %s' % (text_z1d)
        irc.reply(s)

    def w2(self, irc, msg, args):
        """
        KNMI Weerbericht 2
        """
        self._last_channel = msg.channel

        url = "https://www.knmi.nl/nederland-nu/weer/verwachtingen"
        page = utils.web.getUrl(url, headers=HEADERS).decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        text_x2 = soup.select_one('.weather__text > p:nth-child(3)').text
        text_y2 = BeautifulSoup(text_x2, 'html.parser').getText()
        text_z2a = text_y2.replace("\xa0", " ")
        text_z2b = text_z2a.replace("Waarschuwingen Er zijn geen waarschuwingen", "")
        text_z2c = text_z2b.replace("Vanochtend", "\x02Vanochtend\x02")
        text_z2d = text_z2c.replace(".Vanmiddag", ". \x02Vanmiddag\x02")
        text_z2e = text_z2d.replace(".Vanavond", ". \x02Vanavond\x02")
        text_z2f = text_z2e.replace("Morgenochtend", "\x02Morgenochtend\x02")
        text_z2g = text_z2f.replace(".Morgenmiddag", ". \x02Morgenmiddag\x02")
        text_z2h = text_z2g.replace(".Morgenavond", ". \x02Morgenavond\x02")
        s = '(2) %s' % (text_z2h)
        irc.reply(s)

    def w3(self, irc, msg, args):
        """
        KNMI Weerbericht 3
        """
        self._last_channel = msg.channel

        url = "https://www.knmi.nl/nederland-nu/weer/verwachtingen"
        page = utils.web.getUrl(url, headers=HEADERS).decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        text_x3 = soup.select_one('.weather__text > p:nth-child(4)').text
        text_y3 = BeautifulSoup(text_x3, 'html.parser').getText()
        text_z3a = text_y3.replace("\xa0", " ")
        text_z3b = text_z3a.replace("Vanochtend", "\x02Vanochtend\x02")
        text_z3c = text_z3b.replace(".Vanmiddag", ". \x02Vanmiddag\x02")
        text_z3d = text_z3c.replace(".Vanavond", ". \x02Vanavond\x02")
        text_z3e = text_z3d.replace("Morgenochtend", "\x02Morgenochtend\x02")
        text_z3f = text_z3e.replace(".Morgenmiddag", ". \x02Morgenmiddag\x02")
        text_z3g = text_z3f.replace(".Morgenavond", ". \x02Morgenavond\x02")
        s = '(3) %s' % (text_z3g)
        irc.reply(s)

    def w4(self, irc, msg, args):
        """
        KNMI Weerbericht 4
        """
        self._last_channel = msg.channel

        url = "https://www.knmi.nl/nederland-nu/weer/verwachtingen"
        page = utils.web.getUrl(url, headers=HEADERS).decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        text_x4 = soup.select_one('.weather__text > p:nth-child(5)').text
        text_y4 = BeautifulSoup(text_x4, 'html.parser').getText()
        text_z4a = text_y4.replace("\xa0", " ")
        text_z4b = text_z4a.replace("Vanochtend", "\x02Vanochtend\x02")
        text_z4c = text_z4b.replace(".Vanmiddag", ". \x02Vanmiddag\x02")
        text_z4d = text_z4c.replace(".Vanavond", ". \x02Vanavond\x02")
        text_z4e = text_z4d.replace("Morgenochtend", "\x02Morgenochtend\x02")
        text_z4f = text_z4e.replace(".Morgenmiddag", ". \x02Morgenmiddag\x02")
        text_z4g = text_z4f.replace(".Morgenavond", ". \x02Morgenavond\x02")
        s = '(4) %s' % (text_z4g)
        irc.reply(s)

    def w5(self, irc, msg, args):
        """
        KNMI Weerbericht 5
        """
        self._last_channel = msg.channel

        url = "https://www.knmi.nl/nederland-nu/weer/verwachtingen"
        page = utils.web.getUrl(url, headers=HEADERS).decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        text_x5 = soup.select_one('.weather__text > p:nth-child(6)').text
        text_y5 = BeautifulSoup(text_x5, 'html.parser').getText()
        text_z5a = text_y5.replace("\xa0", " ")
        text_z5b = text_z5a.replace("Vanochtend", "\x02Vanochtend\x02")
        text_z5c = text_z5b.replace(".Vanmiddag", ". \x02Vanmiddag\x02")
        text_z5d = text_z5c.replace(".Vanavond", ". \x02Vanavond\x02")
        text_z5e = text_z5d.replace("Morgenochtend", "\x02Morgenochtend\x02")
        text_z5f = text_z5e.replace(".Morgenmiddag", ". \x02Morgenmiddag\x02")
        text_z5g = text_z5f.replace(".Morgenavond", ". \x02Morgenavond\x02")
        s = '(5) %s' % (text_z5g)
        irc.reply(s)


Class = KNMI


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
