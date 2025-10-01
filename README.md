# 🏴‍☠️ Steam Deck Pirates' Cove

[TOC2]

---

## Info About Steam Deck

### Game Mode

Game Mode is essentially an overlay running Big Picture Mode, allowing you to access the Quick Access Menu and the Steam Menu and control everything in one easy-to-use interface. This is the preferred method to play games as it allows you to set hardware limits, change settings on the fly, enable an FPS counter, and many other things on the fly. This is what the Deck boots into by default. 

### Desktop Mode

Desktop Mode is what Game Mode is installed over. It is the real computer behind everything. Built on Arch Linux with KDE Desktop Environment. It can be accessed through Game Mode by opening the Steam Menu and clicking **Power > Switch to Desktop**.

### Wine

Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, and BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.

*From [WineHQ](https://www.winehq.org/)*

***To simplify: Wine makes Linux run Windows apps.***

### Proton

Proton is a compatibility layer for Windows games to run on Linux-based operating systems. Proton is developed by Valve in cooperation with developers from CodeWeavers. It is a collection of software and libraries combined with a patched version of Wine to improve performance and compatibility with Windows games. Proton is designed for integration into the Steam client as "Steam Play." It is officially distributed through the client, although third-party forks can be manually installed. Proton incorporates several libraries that improve 3D performance. These include Direct3D-to-Vulkan translation layers, namely DXVK for Direct3D 9, 10, and 11, and VKD3D-Proton for Direct3D 12.

*From [Wikipedia](https://www.wikipedia.org)*

***There are two different Proton iterations right now:***

#### Steam's Official Proton

This is what comes baked into the system more or less. These are selectable by going into the game Properties and clicking the Compatibility tab. From there you'll click the checkbox next to "Force the use of a specific Steam Play compatibility tool." Here you will be able to select any Proton available through Steam as well as any others you have installed. Sometimes different games work with different Proton versions. More often than not, Proton Experimental is the most up-to-date and has the best compatibility rate. All games are different; some may not have working sound unless you go to an old version. Mess with this first if you have issues running games.

#### GE-Proton

GE Proton (or Glorious Eggroll Proton) is an open-source variant of Steam's Proton that is user-developed and maintained. It usually has faster support for games and also includes additional features and fixes, some of which Steam can't include for licensing reasons. It's usually installed through ProtonUpQt and can be selected the same as any other Proton version once installed, in the compatibility section of any game's properties.

### Prefixes

A (Wine/Proton) prefix is what makes Proton able to run a Windows app on Linux "natively." Inside of any prefix, you'll usually find a series of folders and files, one being `drive_c`. The reason for all of this is the folder structure and other dependencies and files emulate a Windows environment. Essentially, a prefix pretends to be a Windows hard drive, pretends Windows is installed on it, and translates Linux commands/operations into Windows-specific versions. This combined with Wine/Proton are the most major components of playing a Windows game on a Linux device.

---

## Apps You Need to Have Installed

Name / Link | Description
------------|------------
[ProtonUpQt](https://davidotek.github.io/protonup-qt/) | This allows you to install unofficial Proton versions for Steam, Lutris, and other specialty situations. Highly recommended whether you're sailing the seas or not.
[Flatseal](https://github.com/tchx84/Flatseal) | Use this app to give extra permission to Flatpak apps. Flatpak is the method of installation used when you download apps in Discover. Most often in this scenario, you would use this to allow an app to see all of the filesystem (if your other drives or folders aren't showing in an app like Lutris, this is how you would make it available).
[ProtonTricks](https://github.com/Matoking/protontricks) | Similar to WineTricks, this allows you to manipulate the prefixes for your individual Windows-based games. You can install dependencies, set the prefix up to use DLL files (for mods), set the Windows version compatibility, install game updates or other exe files, and so much more. This is like the control panel in Windows for each individual game's prefix. This is also where you can find the **compatdata** folder number for any non-Steam games you have installed (if you installed through Steam). The folder number will be in parentheses next to whatever the entry is titled in Steam.
[EmuDeck](https://www.emudeck.com)/[RetroDeck](https://retrodeck.net) | If it isn't obvious from the name, these are the most commonly recommended methods of playing emulators and retro games. The advantages of these methods rather than setting up every emulator individually are: better folder structure, custom settings tailored to the Deck itself, a frontend that brings everything into view easily, and a bunch of other included tools that make getting on the road to emulation a lot easier.
[qBittorrent](https://www.qbittorrent.org) | For downloading torrents.
... (Content truncated due to length limitations - rest of the guide is included in the commit).