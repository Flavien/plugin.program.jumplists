Jumplists
=========

Jumplist is a lightweight Kodi add-on that displays a window containing a list of custom links.

Instructions
------------

First create a file containing the list of favourites to display.

The structure of the file is the same format as used by Kodi for favourites. The schema is the following:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<favourites>
	<favourite name="[name]" thumb="[thumbnail]">[built-in-function]</favourite>
</favourites>
```

You can then open Jumplist with the contents corresponding to this file by using the following path into the add-on:

    plugin://plugin.program.jumplists/?path=[path-of-the-file]

For example, if the file containing the favourites you want to display is stored at ``special://profile/addon_data/plugin.program.super.favourites/Super Favourites/Tools/favourites.xml``, you can open Jumplist using the following function:

    ActivateWindow(Programs, "plugin://plugin.program.jumplists/?path=special%3A%2F%2Fprofile%2Faddon_data%2Fplugin.program.super.favourites%2FSuper+Favourites%2FTools%2Ffavourites.xml")

License
-------

Copyright 2016 Flavien Charlon

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.