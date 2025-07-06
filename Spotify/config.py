###
# Copyright (c) 2010, Terje Hoås
# Copyright (c) 2025, Dorian Harmans
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

from supybot import conf, registry
    
try:
    from supybot.i18n import PluginInternationalization

    _ = PluginInternationalization("Spotify")
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Spotify', True)


Spotify = conf.registerPlugin('Spotify')

conf.registerGlobalValue(Spotify, 'client_id',
    registry.String("", _("""Your Spotify Client ID (required)"""), private=True))
conf.registerGlobalValue(Spotify, 'client_secret',
    registry.String("", _("""Your Spotify Client secret (required)"""), private=True))

conf.registerChannelValue(Spotify, 'prefix',
    registry.String("^ \x02\x039,1Spotify\x03\x02", _("""Prefix when responding.""")))
conf.registerChannelValue(Spotify, 'titlewhenhttp',
    registry.Boolean(True, _("""Respond on Spotify HTTP-urls aswell""")))
conf.registerChannelValue(Spotify, 'outputurl',
    registry.Boolean(True, _("""Output HTTP url on Spotify uri""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
