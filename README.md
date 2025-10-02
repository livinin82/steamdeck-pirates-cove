# 🏴‍☠️ Steam Deck Pirates' Cove 🏴‍☠️

---

## Table of Contents
- [Info About Steam Deck](#info-about-steam-deck)
- [Apps You Need](#apps-you-need)
- [Guides for Installing Games](#guides-for-installing-games)
- [Guides for Proton/Wine](#guides-for-protonwine)
- [Guides for Emulators and ROMs](#guides-for-emulators-and-roms)
- [Cracks/DLC/Updates](#cracksdlcupdates)
- [Common Questions](#common-questionsthings-you-will-encounter)
- [Other Subreddits/Groups](#other-subredditsgroups)
- [Useful Links](#useful-links)

---

## Info About Steam Deck

### Game Mode

Game Mode is essentially an overlay running Big Picture Mode, allowing you to access the Quick Access Menu and the Steam Menu and control everything in one easy to use interface. This is the preferred method to play games as it allows you to set hardware limits, change settings on the fly, enable a fps counter, and many other things on the fly. This is what the Deck boots into by default.

### Desktop Mode

Desktop Mode is what Game Mode is installed over. It is the real computer behind everything. Built on Arch Linux with KDE Desktop Environment. It can be accessed through Game Mode by opening the Steam Menu and clicking **Power > Switch to Desktop**.

### Wine

Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.

*from [WineHQ](https://www.winehq.org/)*

**Note:** To simplify: Wine makes Linux run Windows apps.

### Proton

Proton is a compatibility layer for Windows games to run on Linux-based operating systems. Proton is developed by Valve in cooperation with developers from CodeWeavers. It is a collection of software and libraries combined with a patched version of Wine to improve performance and compatibility with Windows games. Proton is designed for integration into the Steam client as "Steam Play". It is officially distributed through the client, although third-party forks can be manually installed. Proton incorporates several libraries that improve 3D performance. These include Direct3D-to-Vulkan translation layers, namely DXVK for Direct3D 9, 10 and 11, and VKD3D-Proton for Direct3D 12.

*from [Wikipedia](https://www.wikipedia.org)*

**There are two different Proton iterations right now:**

#### Steam's Official Proton

This is what comes baked into the system more or less. These are selectable by going into the game Properties and clicking the Compatibility tab. From there you'll click the checkbox next to "Force the use of a specific Steam Play compatibility tool." Here you will be able to select any Proton available through steam as well as any others you have installed. Sometimes different games work with different Proton versions. More often than not Proton Experimental is the most up to date and has the best compatibility rate. All games are different, some may not have working sound unless you go to an old version. Mess with this first if you have issues running games.

#### GE-Proton

GE Proton (Glorious Eggroll Proton) is an open source variant of Steams Proton that is user developed and maintained. It usually has faster support for games and also includes additional features and fixes, some which Steam can't include for licensing reasons. It's usually installed through ProtonUpQt, and can be selected the same as any other Proton version once installed, in the compatibility section of any game's properties.

### Prefixes

A (Wine/Proton) prefix is what makes Proton able to run a Windows app on Linux "natively". Inside of any prefix you'll usually find a series of folders and files, one being drive_c. The reason for all of this is the folder structure and other dependencies and files emulates a Windows environment. Essentially a prefix pretends to be a Windows hard drive, pretends Windows is installed on it, and translates Linux commands/operations into Windows specific versions. This combined with Wine/Proton are the most major components of playing a Windows game on a Linux device.

### Launchers

Launchers are apps built for Linux that allow you to play games from other Launcher based game companies. Heroic, Bottles, and Lutris are the main ones. These add a few more things some games may need to run efficiently or properly at all. While these are a preferred method for ease of use, keep in mind this is another layer between your game and SteamOS so at times troubleshooting it may be a little more difficult. These also usually come with Wine configuration, login support for launchers, the option to add shortcuts to Steam, and a whole slew of other features allowing you to do less tinkering and kind of just get going.

### Decky Plugins

*Note: Decky plugins may break with each update and can be the cause of issues at times.*

---

## Apps You Need

*Italicized items are available on the Discover Store.*

| Name/Link | Description |
|-----------|-------------|
| [ProtonUpQt](https://davidotek.github.io/protonup-qt/) | Install unofficial Proton versions for Steam, Lutris, and more. Highly recommended. |
| [Flatseal](https://github.com/tchx84/Flatseal) | Give extra permission to Flatpak apps. Use to allow apps to see all of the filesystem. |
| [ProtonTricks](https://github.com/Matoking/protontricks) | Manipulate prefixes for individual Windows games. Install dependencies, set compatibility, etc. |
| [Bottles](https://usebottles.com), [Lutris](https://lutris.net), [Heroic Launcher](https://heroicgameslauncher.com) | Launchers for organizing and running games from other platforms. |
| [EmuDeck](https://www.emudeck.com), [RetroDeck](https://retrodeck.net) | Recommended methods for emulators and retro games. |
| [Warpinator](https://warpinator.com/warpinator-download/) | File transfer service for your local network. Use [Winpinator](https://winpinator.swisz.cz/) or Warpinator for Windows. |
| [JDownloader](https://jdownloader.org) | Download manager for multi-part links, captchas, etc. |
| [qBittorrent](https://www.qbittorrent.org) | For downloading torrents. |
| [AnyDesk](https://anydesk.com/en), [RustDesk](https://rustdesk.com) | Remote Desktop applications. |
| [PeaZip](https://peazip.github.io) | Application for handling compressed files (.rar, .7z, .zip, etc.). |

**Note:** Do not use BitTorrent or uTorrent as they have been known to be shady in the past.

---

## Guides for Installing Games

### Installing games through Steam

**Note:** There are a few different ways to get cracked games on your system. They all for the most part end in the same results. Some games require one method over another. Part of piracy is experimenting and finding what works best. If you find a better method for a specific game let us know in the subreddit!

If your game is already in a preinstalled state, skip to **Part 3**.

#### Part 1: Running the setup.exe

**Method 1: Using Wine**
- Right-click setup.exe and select Wine.
- Limit the installer to 2GB of RAM.
- Install to your preferred location for games.

**Method 2: Using Steam Compatibility Tool**
- Switch your Steam Deck to desktop mode (in the Power settings menu).
- Locate the downloaded game and the setup.exe file.
- Right-click on setup.exe and click “Add to Steam”.
- Open Steam, go to your Library, and click on setup.exe.
- Go to the Compatibility section and check the box for “Force the use of a specific compatibility tool.”
- Select Proton Experimental.
- Create a new folder called Games in `/home/deck/`.
- Go back to Steam, click on setup.exe, and press Play.


Wait for the installation to complete. Once done, check off all the radio boxes in the installer and close it.

**Note:** FG repacks default to the D drive, and DoDi repacks default to the C drive.

#### Part 2: Installation

Be patient. Sometimes, it can take a while for the installer to appear.

- Once it does, select your preferred language (e.g., English) and click Next.
- Follow the installer steps. Make sure to:
  - Set the installation path to the Games folder in the Z drive (or your microSD card if installing there).
  - Untick any options for additional installations (like DirectX and Visual C++).
