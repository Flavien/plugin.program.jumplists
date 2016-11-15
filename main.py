# Copyright 2016 Flavien Charlon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xbmcswift2
import xbmc
import xbmcaddon
import xbmcvfs
import xml.etree.ElementTree

plugin = xbmcswift2.Plugin()
big_list_view = False
root_launch = True

def log(v):
    xbmc.log(repr(v))

@plugin.route('/execute/<url>')
def execute(url):
    xbmc.executebuiltin(url)

@plugin.route('/jumplist')
def jumplist():
    if not "path" in plugin.request.args:
        return None

    path = plugin.request.args["path"][0]
    
    file_path = xbmc.translatePath(path)

    root = xml.etree.ElementTree.parse(file_path).getroot()

    return [
    {
        'label': favourite.attrib["name"],
        'path': plugin.url_for('execute', url = favourite.text),
        'thumbnail': favourite.attrib["thumb"]
    }
    for favourite in root.findall("./favourite")]

@plugin.route('/')
def index():
    #if root_launch:
    #    folder_path = "special://profile/addon_data/plugin.program.super.favourites/Super Favourites/"
    #    return jumplists(folder_path)
    #else:
    log("index")
    return None

@plugin.route('/jumplists/<path>')
def jumplists(path=None):
    items = []

    folders, files = xbmcvfs.listdir(path)
    for folder in sorted(folders, key=lambda x: x.lower()):
        folder_path = "%s%s/" % (path, folder)
        thumbnail_file = "%sicon.txt" % folder_path
        thumbnail = xbmcvfs.File(thumbnail_file,"rb").read()

        items.append(
        {
            'label': folder,
            'path': plugin.url_for('jumplist', path="%sfavourites.xml" % (folder_path)),
            'thumbnail':thumbnail,
            'context_menu': [],
        })

    return items


if __name__ == '__main__':

    ADDON = xbmcaddon.Addon()
    version = ADDON.getAddonInfo('version')
    if ADDON.getSetting('version') != version:
        ADDON.setSetting('version', version)

    plugin.run()
    if big_list_view == True:
        view_mode = int(plugin.get_setting('view_mode'))
        plugin.set_view_mode(view_mode)