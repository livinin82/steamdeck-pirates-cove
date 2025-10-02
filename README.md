-----

# 🏴‍☠️ Steam Deck Pirates' Cove 🏴‍☠️

-----

## Info About Steam Deck

### Game Mode

Game Mode is essentially an overlay running Big Picture Mode, allowing you to access the Quick Access Menu and the Steam Menu and control everything in one easy to use interface. This is the preferred method to play games as it allows you to set hardware limits, change settings on the fly, enable a fps counter, and many other things on the fly. This is what the Deck boots into by default.

### Desktop Mode

Desktop Mode is what Game Mode is installed over. It is the real computer behind everything. Built on Arch Linux with KDE Desktop Environment. It can be accessed through Game Mode by opening the Steam Menu and clicking **Power > Switch to Desktop**.

### Wine

Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.

*from [WineHQ](https://www.winehq.org/)*

> To simplify: Wine Makes Linux run Windows apps

### Proton

Proton is a compatibility layer for Windows games to run on Linux-based operating systems. Proton is developed by Valve in cooperation with developers from CodeWeavers. It is a collection of software and libraries combined with a patched version of Wine to improve performance and compatibility with Windows games. Proton is designed for integration into the Steam client as "Steam Play". It is officially distributed through the client, although third-party forks can be manually installed. Proton incorporates several libraries that improve 3D performance. These include Direct3D-to-Vulkan translation layers, namely DXVK for Direct3D 9, 10 and 11, and VKD3D-Proton for Direct3D 12.

*from [Wikipedia](https://www.wikipedia.org)*

***There are two different Proton iterations right now:***

# Steam Deck Pirates' Cove — Documentation Landing

This repository's canonical documentation is the long-form guide: `GUIDE.md`.

Housekeeping: temporary preview artifacts and intermediate .bak files created during migration have been cleaned up. If you need the earlier backups, check Git history.

For full instructions, troubleshooting, and the detailed how-tos, please open:

- GUIDE.md — the canonical guide (recommended)

If you'd prefer the shorter README as the single source, I can delete `GUIDE.md` and promote the README instead — but for now I've made `GUIDE.md` the canonical document and kept this README intentionally minimal so the project landing is clear.

> [!TIP]
> * Once it does, select your preferred language (e.g., English) and click Next.
> * Follow the installer steps. Make sure to:
>     * Set the installation path to the `Games` folder in the Z drive (or your microSD card if installing there).
>     * Untick any options for additional installations (like DirectX and Visual C++).
> * Start the installation.
>     * Optional step: Limit the installer to 2GB of RAM for installation stability.

> [!NOTE]
>
>   * Don’t worry if the installation is slow, especially for repacks. This is normal and can take hours depending on game size and compression.

##### Part 3: Running the Game

> [!TIP]
> **Method 1: Using Wine**
>
>   * Once the installation is complete, go to the installation folder and locate the game’s `.exe` file (e.g., `game.exe`).
>   * Right-click on the `game.exe`, select “Add to Steam” to add it as a non-Steam game.
>   * Open Steam, find `game.exe`, and go to the Compatibility section.
>   * Set the compatibility to Proton Experimental.
>   * Launch the game by pressing Play.
>   * If it shows an error or doesn’t run: Refer to the dependencies guide for help (Dependencies Guide).
>   * Run the game in Desktop mode to verify it works correctly.
>   * Once verified, you can rename it in Steam to whatever you prefer, and then switch back to Gaming mode to play.

> [!TIP]
> **Method 2: Using Steam Compatibility Tool**
>
>   * Once the installation is complete, go back to Steam and remove `setup.exe` (right-click > Manage > Remove non-Steam game).
>   * Go to the installation folder, find the `game.exe` file, right-click on it, and add it to Steam.
>   * Open Steam, find `game.exe`, and go to the Compatibility section. Repeat steps 5-7 from Part 1 (set the compatibility to Proton Experimental).
>   * Launch the game by pressing Play.
>   * Run the game in Desktop mode to make sure it works correctly.
>   * Exit the game. You can rename it in Steam to whatever you prefer (otherwise, it’ll show as `game.exe` in gaming mode).
>   * Switch back to Gaming mode and enjoy your game!

> [!NOTE]
>
>   * If it shows an error or doesn’t run: Either the Proton version is incorrect (try different ones) or there’s a missing dependency. If it's the latter, refer to a dependencies guide (Dependencies Guide).

> [!TIP]
> **Additional Notes**
>
>   * Some downloads may come in `.rar` files. Extract these using an app like PeaZip before proceeding to Step 2.
>   * Proton Experimental should usually work, but if it doesn’t, try the latest Proton version or Proton-GE.
>   * You may need to enable hidden files for this step.
>   * To install on a microSD card, create a folder named `Games` on the SD card root. Then, add the following to `setup.exe`’s launch options:
>     ```bash
>     STEAM_COMPAT_MOUNTS="/run/media/mmcblk0p1/Games/" %command%
>     ```
>   * Avoid installing to the C drive to prevent issues later on.
>   * Some games may have a different `.exe` file for launching. Use Dolphin File Explorer to search for other `.exe` files in the game folder.
>   * Some games require specific Proton versions. Search Reddit for recommendations, and use ProtonUp-QT to download other Proton versions if needed.
>   * This guide should help you install and configure non-Steam games on your Steam Deck. Enjoy gaming!
