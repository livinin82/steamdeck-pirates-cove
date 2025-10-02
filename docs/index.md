# Steam Deck Pirates' Cove# Steam Deck Pirates' Cove



A comprehensive guide for Steam Deck gaming, emulation, and troubleshooting.A comprehensive guide for Steam Deck gaming, emulation, and troubleshooting.



------



## Info About Steam Deck# Steam Deck



### Game Mode## Game/Desktop Mode



Game Mode is essentially an overlay running Big Picture Mode, allowing you to access the Quick Access Menu and the Steam Menu and control everything in one easy to use interface. This is the preferred method to play games as it allows you to set hardware limits, change settings on the fly, enable a fps counter, and many other things on the fly. This is what the Deck boots into by default.- To switch to Desktop Mode, press the `Steam` button, go to `Power`, and select `Switch to Desktop`.

- To return to Game Mode, use the `Return to Game Mode` icon on the Desktop.

### Desktop Mode

## Wine/Proton

Desktop Mode is what Game Mode is installed over. It is the real computer behind everything. Built on Arch Linux with KDE Desktop Environment. It can be accessed through Game Mode by opening the Steam Menu and clicking **Power > Switch to Desktop**.

- The Steam Deck uses a compatibility layer called Proton (a fork of Wine) to run Windows games.

### Wine- Different games may require different Proton versions. You can change the Proton version for a specific game in its `Properties` > `Compatibility` settings in Steam.



Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.---



*from [WineHQ](https://www.winehq.org/)*# Required Apps



> **To simplify: Wine Makes Linux run Windows apps**## ProtonUp-Qt



### Proton- **Installation**: Install `ProtonUp-Qt` from the `Discover` store in Desktop Mode.

- **Usage**:

Proton is a compatibility layer for Windows games to run on Linux-based operating systems. Proton is developed by Valve in cooperation with developers from CodeWeavers. It is a collection of software and libraries combined with a patched version of Wine to improve performance and compatibility with Windows games. Proton is designed for integration into the Steam client as "Steam Play". It is officially distributed through the client, although third-party forks can be manually installed. Proton incorporates several libraries that improve 3D performance. These include Direct3D-to-Vulkan translation layers, namely DXVK for Direct3D 9, 10 and 11, and VKD3D-Proton for Direct3D 12.    - Launch `ProtonUp-Qt`.

    - Click `Add version` to see a list of compatibility tools.

*from [Wikipedia](https://www.wikipedia.org)*    - Install the latest `GE-Proton`.

    - Restart Steam to see the new `GE-Proton` version in the compatibility list.

**There are two different Proton iterations right now:**

## Flatseal

#### Steam's Official Proton

- **Installation**: Install `Flatseal` from the `Discover` store.

This is what comes baked into the system more or less. These are selectable by going into the game Properties and clicking the Compatibility tab. From there you'll click the checkbox next to "Force the use of a specific Steam Play compatibility tool". Here you will be able to select any Proton available through steam as well as any others you have installed. Sometimes different games work with different Proton versions. More often than not Proton Experimental is the most up to date and has the best compatibility rate. All games are different, some may not have working sound unless you go to an old version. Mess with this first if you have issues running games.- **Usage**:

    - `Flatseal` manages Flatpak permissions.

#### GE-Proton    - To grant an application access to an SD card or an external drive:

        1. Open `Flatseal`.

GE Proton (or Glorious Eggroll Proton) is an open source variant of Steams Proton that is user developed and maintained. It usually has faster support for games and also includes additional features and fixes, some which Steam can't include for licensing reasons. It's usually installed through ProtonUpQt, and can be selected the same as any other Proton version once installed, in the compatibility section of any game's properties.        2. Select the application (e.g., Lutris).

        3. Under `Filesystem`, go to `Other files`.

### Prefixes        4. Click the folder icon and add the path to your drive (e.g., `/run/media/mmcblk0p1/` for SD card).



A (Wine/Proton) prefix is what makes Proton able to run a Windows app on Linux "natively". Inside of any prefix you'll usually find a series of folders and files, one being drive_c. The reason for all of this is the folder structure and other dependencies and files emulates a Windows environment. Essentially a prefix pretends to be a Windows hard drive, pretends Windows is installed on it, and translates Linux commands/operations into Windows specific versions. This combined with Wine/Proton are the most major components of playing a Windows game on a Linux device.---



### Launchers# Game Installation



Launchers are apps built for Linux that allow you to play games from other Launcher based game companies. Heroic, Bottles, and Lutris are the mainly discussed ones. These add a few more things some games may need to run efficiently or properly at all. While these are a preferred method for ease of use, keep in mind this is another layer between your game and SteamOS so at times troubleshooting it may be a little more difficult. These also usually come with Wine configuration, login support for launchers, the option to add shortcuts to Steam, and a whole slew of other features allowing you to do less tinkering and kind of just get going.## Steam



### Decky Plugins- **Method**:

    1. Go to the game's `Properties` > `Compatibility`.

---    2. Check `Force the use of a specific Steam Play compatibility tool`.

    3. Select a `Proton` version.

## Required Apps- **Note**: If a game doesn't work, try a different Proton version, especially `GE-Proton`.



> **Note:** Items in *italics* are available on the Discover Store.## Lutris



| Name/Link | Description |- **Installation**:

|-----------|-------------|    1. Install `Lutris` from the `Discover` store.

| *[ProtonUpQt](https://davidotek.github.io/protonup-qt/)* | This allows you to install unofficial Proton versions for Steam, Lutris, and other specialty situations. Highly recommended whether you're sailing the seas or not. |    2. Open `Flatseal`, select `Lutris`, and grant it access to your game library location under `Filesystem`.

| *[Flatseal](https://github.com/tchx84/Flatseal)* | Use this app to give extra permission to Flatpak apps. Flatpak is the method of installation used when you download apps in Discover. Most often in this scenario you would use this to allow an app to see all of the filesystem (if your other drives or folders aren't showing in an app like Lutris, this is how you would make it available). |- **Adding Games**:

| *[ProtonTricks](https://github.com/Matoking/protontricks)* | Similar to WineTricks, this allows you to manipulate the prefixes for your individual Windows based games. You can install dependencies, set the prefix up to use DLL files (for mods), set the Windows versions compatibility, install game updates or other exe files, and so much more. This is like the control panel in Windows for each individual games prefix. This is also where you can find the **compatdata** folder number for any non steam games you have installed (if you installed through steam). The folder number will be in parentheses next to whatever the entry is titled in steam. |    - Click the `+` icon in Lutris and select `Add a locally installed game`.

| *[Bottles](https://usebottles.com)/[Lutris](https://lutris.net)/[Heroic Launcher](https://heroicgameslauncher.com)* | These are the launchers that are mentioned in the previous section. Bottles, Lutris, and Heroic have varied access to the stupid launchers all AAA publishers insist on using. Think of these as mega launcher that allows you to organize and work with a multitude of launcher-based games without having to jump from launcher to launcher. These can all be found on the discover store. |    - **Game Info Tab**:

| [EmuDeck](https://www.emudeck.com)/[RetroDeck](https://retrodeck.net) | If it isn't obvious from the name, these are the most commonly recommended methods of playing emulators and retro games. The advantages of these methods rather than setting up every emulator individually are: better folder structure, custom settings tailored to the Deck itself, a frontend that brings everything into view easily, and a bunch of other included tools that make getting on the road to emulation a lot easier. There is a larger section about emulation below. |        - `Name`: Enter the game's name.

| *[Warpinator](https://warpinator.com/warpinator-download/)* | Warpinator is a recommended file transfer service for your local network. This application works with all OS options. It will need to be running on both your Steam Deck and the device you are transferring files from/to. For Windows there are two options, [Winpinator](https://winpinator.swisz.cz/) and [Warpinator](https://warpinator.com/warpinator-download/). I have personally had more luck with the actual Warpinator. Sometimes if there are connection issues it is best to manually set the network device in settings. This is the fastest and easiest to set up method for transferring files. |        - `Runner`: Choose `Wine`.

| *[JDownloader](https://jdownloader.org)* | A download manager that I myself swear by. It can handle multi part links, fill captchas for you, store account info for sites you have a login with, and it usually finds the highest speed it can. Any type of DL link works here for the most part. It is recommend downloading one or two files at a time through settings so you can maximize speed. |    - **Game Options Tab**:

| *[qBittorrent](https://www.qbittorrent.org)* | For downloading torrents. |        - `Executable`: Path to the game's `.exe` file.

| *[AnyDesk](https://anydesk.com/en)/[RustDesk](https://rustdesk.com)* | These are Remote Desktop applications. Use this to access your desktop mode from another PC or Device that can install these apps. This is great in the absence of a keyboard and mouse, you can also send files to yourself (albeit small ones). This is really useful also if you don't wanna keep switching between monitor inputs while docked, etc. If you want real ease of use be sure to set up unattended access with a password for the remote app so you don't have to use the Deck to accept every session. |        - `Wine prefix`: A separate folder for the game's Wine environment (e.g., `~/Games/Lutris/game-name/`).

| *[PeaZip](https://peazip.github.io)* | Application for handling compressed files. This includes .rar, .7z, .zip, etc. This is especially useful for multipart zip files (repacks/large games) as Dolphin seems to have issues with them. Open PeaZip, click Open, find where your multipart compressed files are, and select one. It should open all of the data inside the window, then click extract and make sure you extract to a place you can find easily! |    - **Runner Options Tab**:

        - Select a `Wine version` (e.g., `GE-Proton`).

> **Warning:** Do not use BitTorrent or uTorrent as they have been known to be shady in the past.- **Adding to Steam**:

    - In Lutris, right-click the game and select `Create Steam shortcut`.

---    - Restart Steam. The game will appear in your library.

    - In Steam, go to the game's `Properties` > `Shortcut` and add `STEAM_COMPAT_DATA_PATH="/path/to/wine/prefix/" %command%` to the `Launch Options`.

## Game Installation

---

```mermaid

graph TD# File Transfers

    A[Source Game]

    B["Install Game on PC"]## SSH

    C["Pre-installed Game"]

    D["Install Game on SteamDeck"]- **Setup**:

    E["Transfer to Steam Deck"]    1. In Desktop Mode, open `Konsole`.

    F["Add Non-Steam Game"]    2. Set a password with `passwd`.

    G{"Set up Windows Environment"}    3. Start the SSH server with `sudo systemctl start sshd`.

    H["Configure with ProtonTricks"]- **Usage**:

    Z((Play Game))    - Use an SFTP client like `WinSCP` (Windows) or `FileZilla` (cross-platform).

    - Connect to your Steam Deck's IP address (found in `System Settings` > `Network`).

    A --> B

    A --> C## Warpinator

    A --> D

    B --> E- **Installation**:

    C --> E    - Install `Warpinator` from the `Discover` store on your Steam Deck.

    E --> F    - Install `Warpinator` on your PC (available for Linux and Windows).

    D --> F- **Usage**:

    F --> G    - Ensure both devices are on the same network.

    G -- SteamOS --> H    - Open `Warpinator` on both devices. They should automatically detect each other.

    G -- Lutris --> Z    - Select the files you want to transfer.

    H --> Z

```---



### Installing games through Steam# Dependency Management



> **Note:** There are a few different ways to get cracked games on your system. They all for the most part end in the same results. Some games require one method over another. Part of piracy is experimenting and finding what works best. If you find a better method for a specific game let us know in the subreddit!## ProtonTricks



> **If your game is already in a preinstalled state, skip to Part 3.**- **Installation**: Install `ProtonTricks` from the `Discover` store.

- **Usage**:

#### Part 1: Running the setup.exe    - Launch `ProtonTricks`.

    - Select a game to manage its Wine prefix.

**Method 1: Using Wine**    - You can:

- Right-click setup.exe and select Wine        - `Install a Windows DLL or component`.

- Limit the installer to 2GB of RAM        - `Run winecfg` to change Wine settings.

- Install to your preferred location for games        - `Run explorer` to browse the game's C: drive.



**Method 2: Using Steam Compatibility Tool**---

- Switch your Steam Deck to desktop mode (in the Power settings menu)

- Locate the downloaded game and the setup.exe file# Emulation

- Right-click on setup.exe and click "Add to Steam". You'll see a small Steam icon next to your cursor to confirm this step was done correctly

- Open Steam, go to your Library, and click on setup.exe## EmuDeck

- Locate the cog icon on the right side of the screen and click it

- Go to the Compatibility section and check the box that says "Force the use of a specific compatibility tool"- **Installation**:

- Select Proton Experimental    1. Download the `EmuDeck` installer from their website.

- Open Dolphin File Explorer and go to `/home/deck/`. In this path, create a new folder called Games    2. Run the installer in Desktop Mode.

- Go back to Steam, click on setup.exe, and press Play    3. Follow the on-screen instructions to configure emulators and paths.

- **Adding ROMs**:

**Continued from either method:**    - Place your ROMs in the `Emulation/roms` folder on your SD card or internal storage.

- Wait for the installation to complete- **Steam ROM Manager**:

- Once done, check off all the radio boxes in the installer and close it    - EmuDeck uses `Steam ROM Manager` to add emulated games to your Steam library.

    - Run it, and it will automatically generate artwork and shortcuts.

> **Warning:** FG repacks default to the D drive, and DoDi repacks default to the C drive.

## RetroDeck

#### Part 2: Installation

- **Installation**: Install `RetroDeck` from the `Discover` store.

> **Be patient. Sometimes, it can take a while for the installer to appear.**- **Configuration**:

    - On first launch, it will create a folder structure for BIOS files and ROMs.

1. Once it does, select your preferred language (e.g., English) and click Next    - Place BIOS files in `~/.var/app/net.retrodeck.retrodeck/data/retrodeck/bios`.

2. Follow the installer steps. Make sure to:    - Place ROMs in `~/.var/app/net.retrodeck.retrodeck/data/retrodeck/roms`.

   - Set the installation path to the Games folder in the Z drive (or your microSD card if installing there)- **Adding to Steam**:

   - Untick any options for additional installations (like DirectX and Visual C++)    - `RetroDeck` can be added to Steam as a non-Steam game for easy access from Game Mode.

3. Start the installation

   - Optional step: Limit the installer to 2GB of RAM for installation stability---



> **Note:** Don't worry if the installation is slow, especially for repacks. This is normal and can take hours depending on game size and compression.# Troubleshooting



#### Part 3: Running the Game- **Game Not Launching**:

    - Try a different Proton version.

**Method 1: Using Wine**    - Check if all dependencies are installed using `ProtonTricks`.

- Once the installation is complete, go to the installation folder and locate the game's .exe file (e.g., game.exe)- **Performance Issues**:

- Right-click on the game.exe, select "Add to Steam" to add it as a non-Steam game    - Lower in-game settings.

- Open Steam, find game.exe, and go to the Compatibility section    - Use the Steam Deck's built-in performance overlay to monitor FPS and system usage.

- Set the compatibility to Proton Experimental- **Controls Not Working**:

- Launch the game by pressing Play    - Use Steam's controller configuration to map controls.

- If it shows an error or doesn't run: Refer to the dependencies guide for help    - For non-Steam games, ensure Steam Input is enabled.

- Run the game in Desktop mode to verify it works correctly

- Once verified, you can rename it in Steam to whatever you prefer, and then switch back to Gaming mode to play---


**Method 2: Using Steam Compatibility Tool**
- Once the installation is complete, go back to Steam and remove setup.exe (right-click > Manage > Remove non-Steam game)
- Go to the installation folder, find the game.exe file, right-click on it, and add it to Steam
- Open Steam, find game.exe, and go to the Compatibility section. Repeat steps 5-7 from Part 1 (set the compatibility to Proton Experimental)
- Launch the game by pressing Play
- Run the game in Desktop mode to make sure it works correctly
- Exit the game. You can rename it in Steam to whatever you prefer (otherwise, it'll show as game.exe in gaming mode)
- Switch back to Gaming mode and enjoy your game!

> **Note:** If it shows an error or doesn't run: Either the Proton version is incorrect (try different ones) or there's a missing dependency. If it's the latter, refer to a dependencies guide.

**Additional Notes:**
- Some downloads may come in .rar files. Extract these using an app like PeaZip before proceeding to Step 2
- Proton Experimental should usually work, but if it doesn't, try the latest Proton version or Proton-GE
- You may need to enable hidden files for this step
- To install on a microSD card, create a folder named Games on the SD card root. Then, add the following to setup.exe's launch options: `STEAM_COMPAT_MOUNTS="/run/media/mmcblk0p1/Games/" %command%`
- Avoid installing to the C drive to prevent issues later on
- Some games may have a different .exe file for launching. Use Dolphin File Explorer to search for other .exe files in the game folder
- Some games require specific Proton versions. Search Reddit for recommendations, and use ProtonUp-QT to download other Proton versions if needed

### Installing games through Lutris

> **Warning:** Make sure Lutris has access to the filesystem. This can be done through Flatseal. If your Lutris games aren't saving, this is probably why.

> **Note:** It's not necessary to install a game using Lutris as described here. But for some (cracked) games it works better or as described below is necessary insofar as you need a different runner for e.g. the installation of FitGirl repacks. So if you have an already installed game, skip steps 6 to 12.

1. Obtain your desired game from a respected source
2. Install Lutris and open it
3. Click on to top left "+"-button to add a game
4. Enter the name of the game and select the Runner "Wine"
5. Change to the tab "Game options"
6. Click on the top right button "Browse.." to select the game's executable
7. Browse to the directory of your downloaded game and select the installer's *.exe
8. Click "Save", you'll see your game's installation has been added to Lutris
9. Double-click on it or use the bottom-left button "Play"
10. The installation should start, follow the on-screen instructions
11. After the installation is done, right-click the game in Lutris and click "Configure"
12. Go to "Game options" and click the top right button "Browse.."
13. Browse to the directory in which you've installed the game
14. Select the game's executable and click the bottom right "Save"
15. Double-click the game in Lutris to start it or use the bottom left button "Play"

> **Note:** If a game doesn't work or has poor performance, click "Configure" on the game and tick the bottom left box "Show advanced options". Now you can edit the game's options, change the runner, etc.

*from [r/LinuxCrackSupport](https://www.reddit.com/r/LinuxCrackSupport/wiki/index/howto/#wiki_3.2_using_lutris)*

---

## File Transfers

### SSH Setup

#### Setting up SSH on Steam Deck

1. Switch to Desktop Mode: Press the **STEAM** button → **Power** → **Switch to Desktop**
2. Open Konsole: Click **Application Launcher** (bottom left) → **All Applications** → **Konsole**
3. Set a password: Run `passwd` and enter a secure password
4. Enable SSH: Run `sudo systemctl enable sshd`
5. Start SSH: Run `sudo systemctl start sshd`
6. Verify SSH is running: Run `sudo systemctl status sshd`
   - Look for `enabled;` on the `Loaded:` line
   - Look for `active (running)` on the `Active:` line

> **Important:** The password set here will be your password for all Deck operations. Remember it!

#### Connecting from Different Operating Systems

**Windows:**
- Use [WinSCP](https://winscp.net/) for file transfers or [PuTTY](https://putty.org/) for terminal access
- Host: Your Steam Deck's IP address (found in Settings → Internet)
- Username: `deck`
- Password: The one you set with `passwd`
- Port: `22`

**macOS:**
- Built-in support via Terminal or Finder
- Terminal: `ssh deck@[DECK_IP_ADDRESS]`
- Finder: Go → Connect to Server → `sftp://deck@[DECK_IP_ADDRESS]`

**Linux:**
- Built-in support via terminal or file manager
- Terminal: `ssh deck@[DECK_IP_ADDRESS]`
- File manager: Connect to `sftp://deck@[DECK_IP_ADDRESS]`

### Warpinator

Warpinator is an app available for Windows, macOS, and Linux that makes a direct tunnel between your two devices. This is by far the highest speed option outside of SSH.

#### On Your Deck
1. Install **Warpinator** from the **Discover Store**
2. Open **Preferences** and click **Connection** then set a unique PIN
3. In the **General** tab, make sure you point the download folder to a place you can find. I chose my **Games** folder
   - If you don't have access to a certain location (like your SD card), use Flatseal to give Warpinator Permissions

#### On your PC/Mac
1. Download Warpinator from the [official website](https://warpinator.com/warpinator-download/)
2. Install and open it
3. Click **Options → Settings**
4. Put the same PIN from your Deck in the **Group code** box
5. Also make sure your **Receive into folder** is somewhere you can find it
6. Click **Apply**, then click **OK**

#### Transferring Files
1. Your Deck should show in the **Available Devices** area. If not, make sure you followed the steps above. Click on it to open its transfer window
2. On Windows/Mac you can click the `+` button to add a folder, or the `Browse` button to add a singular file. You can also drag and drop multiple folders into the window
3. Accept the transfer on the deck
4. Watch the files fly across your network onto your Deck

> **Tips:**
> - You can go into settings and click **Automatically accept incoming transfers** if you don't want to accept every time
> - If you can't find your device, go into connection settings and select your specific Network device (wifi, ethernet, etc.)

---

## Dependencies and Troubleshooting

### Finding Non-Steam Game Proton Folder

> **Note:** This only works for games added to steam already as a non steam game. This means you need to enable proton on the game and try to run it once so it can set up a prefix for it.

1. Open **ProtonTricks**
2. In the list of games find the title you gave your game in Steam itself
3. Next to the game name, there is a long number
4. Open **Dolphin**
5. Go to `/home/deck/.local/share/Steam/steamapps/compatdata` and find the number from earlier
6. Enter the folder, then enter the `pfx` folder
7. `drive_c` is the folder a lot of the "wine" aspect of things will happen

> **Tips:**
> - Sometimes games will use either `Program Files` or `Program Files (x86)`. Check both
> - In ProtonTricks, your game will show as whatever it is titled in Steam upon opening. If you never changed the name from `setup.exe` then that's what it will be named
> - If you selected `C:` during an install (which you shouldn't have done!), your game may be installed in one of these folders

### Installing Dependencies

Dependencies are other tools/apps that software relies on to work. These are often included in the game installers on official releases. When you add a non-steam game from a pirated package, they may include these in a separate folder, or they may not be included at all.

**Dependencies are needed if:**
- Video/audio is messed up or not working
- Error at beginning stating a certain file or app cannot be found
- The game doesn't start

#### Using ProtonTricks

1. **Open Protontricks:** Launch Protontricks from your applications menu
2. **Select the Game:** Protontricks will show a list of games installed on your Deck. Select the game for which you need to install dependencies
3. **Choose "Select the default wineprefix"** to set up a unique configuration environment for that game
4. **Install Dependencies:** Select **Install a Windows DLL or component** and choose the required dependencies from the list

Common dependencies that games may need:
- **DirectX:** `d3dx9`, `d3dx10`, `d3dx11`
- **Visual C++ Redistributables:** `vcrun2005`, `vcrun2008`, `vcrun2010`, `vcrun2013`, `vcrun2019`
- **DotNet Frameworks:** `dotnet20`, `dotnet40`, `dotnet48`

5. **Verify Installations:** Once installed, Protontricks will confirm the installation of each component

---

## Common Issues and Solutions

### Controller Not Working

**Steam Input Solution:**
1. In **Desktop Mode**, select your game in Steam
2. Click on the gear icon to the right of the **Play** button
3. Click **Properties**
4. Select the **Controller** tab
5. Next to `Override for [Game Name]` click the dropdown
6. Select `Disable Steam Input`

### Game Won't Launch

**Check Proton:**
- Always make sure you have a **Proton** version of some sort enabled
- Try different Proton versions (Experimental, GE-Proton, etc.)

**Check File Paths:**
- Make sure there are quotes around paths with spaces: `"/home/deck/Games/Game Name"`

**Install Dependencies:**
- Use ProtonTricks to install missing dependencies

### Can't See External Drives

**Use Flatseal:**
1. Install **FlatSeal** from the **Discover Store**
2. Open **FlatSeal**
3. Select the app in question (e.g., **Lutris**)
4. Scroll down to **Filesystem**
5. Turn on the switch for `All user files` to permit access to your internal SSD files
6. To see external devices, click the folder icon next to `Other files` and add the path to your device

---

## Emulation

### EmuDeck

EmuDeck is a collection of scripts that allows you to autoconfigure your Steam Deck, it creates your roms directory structure and downloads all of the needed Emulators for you along with the best configurations for each of them.

#### Installing EmuDeck

1. If you are using an SD Card, format your SD Card in Game Mode on SteamOS
2. Switch to Desktop Mode
3. Download the [EmuDeck Installer](https://www.emudeck.com/#download)
4. Copy the installer to your Steam Deck's desktop and run it
5. Copy your games to the `Emulation/roms` folder created by the installer
6. Copy your BIOS to `Emulation/bios`
7. Open Steam ROM Manager through EmuDeck
8. Enable the parsers you want to use
9. Click **Preview** → **Parse** → **Save apps to Steam**
10. Return to Game Mode and enjoy!

### RetroDeck

RetroDECK is an all-in-one Flatpak application that includes emulators and game engines in one pre-configured package.

#### Installing RetroDeck

1. Put the Steam Deck into **Desktop Mode**
2. Install **RetroDECK** from **Discover**
3. Start RetroDECK first time in **Desktop Mode**
4. Choose where RetroDECK should create the roms folders **Internal** or **SDCard**
5. Put the **BIOS files** inside `~/retrodeck/bios/`
6. Put the **ROMS** inside `~/retrodeck/roms/` or custom location
7. Add RetroDECK to Steam as a non-Steam game
8. Switch to **Game Mode** and apply official controller layouts
9. Launch **RetroDECK** and enjoy

---

## Useful Links

- [ProtonDB](https://protondb.com/) - Game compatibility database
- [SteamDB](https://steamdb.info/) - Steam database for game info and dependencies
- [SteamDeckHQ](https://steamdeckhq.com/) - Steam Deck news and guides
- [PCGamingWiki](https://www.pcgamingwiki.com/wiki/Home) - PC gaming fixes and enhancements

### Community Resources

**Piracy Related:**
- [Linux Crack Tips](https://www.reddit.com/r/LinuxCrackSupport/)
- [Piracy](https://www.reddit.com/r/Piracy)
- [FreeMediaHeckYeah](https://www.reddit.com/r/FREEMEDIAHECKYEAH)