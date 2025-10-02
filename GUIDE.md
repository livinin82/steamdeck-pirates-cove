<!--
Steam Deck Pirates' Cove Guide
Based on: https://rentry.co/steamdeckpiratescove
-->

<h1 align="center" style="color:goldenrod; background:mediumslateblue; padding:10px; border-radius:10px;">
🏴‍☠️ Steam Deck Pirates' Cove 🏴‍☠️
</h1>

## Table of Contents
1. [Info About Steam Deck](#info-about-steam-deck)
2. [Apps You NEED TO Have Installed](#apps-you-need-to-have-installed)
3. [Guides for Installing Games](#guides-for-installing-games)
4. [Transferring Installed Games from PC](#transferring-installed-games-from-pc)
5. [Guides for Proton/Wine](#guides-for-protonwine)
6. [Guides for Emulators and ROMs](#guides-for-emulators-and-roms)
7. [Cracks/DLC/Updates](#cracksdlcupdates)
8. [Common Questions](#common-questions)
9. [Other Subreddits/Groups](#other-subredditsgroups)
10. [Useful Links](#useful-links)

***

<a name="info-about-steam-deck"></a>
## 🕹️ Info About Steam Deck

### Game Mode
Game Mode is essentially an overlay running Big Picture Mode, allowing you to access the Quick Access Menu and the Steam Menu and control everything in one easy-to-use interface. This is the preferred method to play games as it allows you to set hardware limits, change settings on the fly, enable an fps counter, and many other things. This is what the Deck boots into by default.

### Desktop Mode
Desktop Mode is what Game Mode is installed over. It is the real computer behind everything. Built on Arch Linux with KDE Desktop Environment. It can be accessed through Game Mode by opening the Steam Menu and clicking **Power > Switch to Desktop**.

### Wine
Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.

<blockquote>
<i>from <a href="https://www.winehq.org/">WineHQ</a></i>
</blockquote>

<b>To simplify: Wine makes Linux run Windows apps</b>

### Proton
Proton is a compatibility layer for Windows games to run on Linux-based operating systems. Proton is developed by Valve in cooperation with developers from CodeWeavers. It is a collection of software and libraries combined with a patched version of Wine to improve performance and compatibility with Windows games. Proton is designed for integration into the Steam client as "Steam Play". It is officially distributed through the client, although third-party forks can be manually installed. Proton incorporates several libraries that improve 3D performance. These include Direct3D-to-Vulkan translation layers, namely DXVK for Direct3D 9, 10 and 11, and VKD3D-Proton for Direct3D 12.

<blockquote>
<i>from <a href="https://www.wikipedia.org">Wikipedia</a></i>
</blockquote>

<b>There are two different Proton iterations right now:</b>

#### Steam's Official Proton
This is what comes baked into the system more or less. These are selectable by going into the game Properties and clicking the Compatibility tab. From there you'll click the checkbox next to "Force the use of a specific Steam Play compatibility tool." Here you will be able to select any Proton available through Steam as well as any others you have installed. Sometimes different games work with different Proton versions. More often than not Proton Experimental is the most up to date and has the best compatibility rate. All games are different, some may not have working sound unless you go to an old version. Mess with this first if you have issues running games.

#### GE-Proton
GE Proton (or Glorious Eggroll Proton) is an open source variant of Steam's Proton that is user developed and maintained. It usually has faster support for games and also includes additional features and fixes, some which Steam can't include for licensing reasons. It's usually installed through ProtonUpQt, and can be selected the same as any other Proton version once installed, in the compatibility section of any game's properties.

### Prefixes
A (Wine/Proton) prefix is what makes Proton able to run a Windows app on Linux "natively". Inside of any prefix you'll usually find a series of folders and files, one being drive_c. The reason for all of this is the folder structure and other dependencies and files emulates a Windows environment. Essentially a prefix pretends to be a Windows hard drive, pretends Windows is installed on it, and translates Linux commands/operations into Windows specific versions. This combined with Wine/Proton are the most major components of playing a Windows game on a Linux device.

### Launchers
Launchers are apps built for Linux that allow you to play games from other Launcher based game companies. Heroic, Bottles, and Lutris are the mainly discussed ones. These add a few more things some games may need to run efficiently or properly at all. While these are a preferred method for ease of use, keep in mind this is another layer between your game and SteamOS so at times troubleshooting it may be a little more difficult. These also usually come with Wine configuration, login support for launchers, the option to add shortcuts to Steam, and a whole slew of other features allowing you to do less tinkering and kind of just get going.

### Decky Plugins
[//]: (Talk about them breaking with each update and being the cause of issues at times)

<!-- Example of warning block using HTML -->
<div style="background:goldenrod; color:black; padding:10px; border-radius:8px; border:2px solid #444;">
<b>⚠️ WARNING:</b> FG repacks default to the D drive, and DoDi repacks default to the C drive.
</div>

<!-- Continue converting the rest of your guide using the above conventions... -->
