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
import xml.etree.ElementTree

plugin = xbmcswift2.Plugin()

@plugin.route('/execute/<url>')
def execute(url):
    xbmc.executebuiltin(url)

@plugin.route('/')
def index():
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


if __name__ == '__main__':
    plugin.run()
