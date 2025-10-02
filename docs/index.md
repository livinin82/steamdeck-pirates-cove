# Steam Deck Pirates' Cove

This file has been moved from GUIDE.md to docs/index.md for GitHub Pages setup.

<details>
<summary>Pirates Cove Guide</summary>

---

%TOC%

---

# Steam Deck

## Game/Desktop Mode

- To switch to Desktop Mode, press the `Steam` button, go to `Power`, and select `Switch to Desktop`.
- To return to Game Mode, use the `Return to Game Mode` icon on the Desktop.

## Wine/Proton

- The Steam Deck uses a compatibility layer called Proton (a fork of Wine) to run Windows games.
- Different games may require different Proton versions. You can change the Proton version for a specific game in its `Properties` > `Compatibility` settings in Steam.

---

# Required Apps

## ProtonUp-Qt

- **Installation**: Install `ProtonUp-Qt` from the `Discover` store in Desktop Mode.
- **Usage**:
    - Launch `ProtonUp-Qt`.
    - Click `Add version` to see a list of compatibility tools.
    - Install the latest `GE-Proton`.
    - Restart Steam to see the new `GE-Proton` version in the compatibility list.

## Flatseal

- **Installation**: Install `Flatseal` from the `Discover` store.
- **Usage**:
    - `Flatseal` manages Flatpak permissions.
    - To grant an application access to an SD card or an external drive:
        1. Open `Flatseal`.
        2. Select the application (e.g., Lutris).
        3. Under `Filesystem`, go to `Other files`.
        4. Click the folder icon and add the path to your drive (e.g., `/run/media/mmcblk0p1/` for SD card).

---

# Game Installation

## Steam

- **Method**:
    1. Go to the game's `Properties` > `Compatibility`.
    2. Check `Force the use of a specific Steam Play compatibility tool`.
    3. Select a `Proton` version.
- **Note**: If a game doesn't work, try a different Proton version, especially `GE-Proton`.

## Lutris

- **Installation**:
    1. Install `Lutris` from the `Discover` store.
    2. Open `Flatseal`, select `Lutris`, and grant it access to your game library location under `Filesystem`.
- **Adding Games**:
    - Click the `+` icon in Lutris and select `Add a locally installed game`.
    - **Game Info Tab**:
        - `Name`: Enter the game's name.
        - `Runner`: Choose `Wine`.
    - **Game Options Tab**:
        - `Executable`: Path to the game's `.exe` file.
        - `Wine prefix`: A separate folder for the game's Wine environment (e.g., `~/Games/Lutris/game-name/`).
    - **Runner Options Tab**:
        - Select a `Wine version` (e.g., `GE-Proton`).
- **Adding to Steam**:
    - In Lutris, right-click the game and select `Create Steam shortcut`.
    - Restart Steam. The game will appear in your library.
    - In Steam, go to the game's `Properties` > `Shortcut` and add `STEAM_COMPAT_DATA_PATH="/path/to/wine/prefix/" %command%` to the `Launch Options`.

---

# File Transfers

## SSH

- **Setup**:
    1. In Desktop Mode, open `Konsole`.
    2. Set a password with `passwd`.
    3. Start the SSH server with `sudo systemctl start sshd`.
- **Usage**:
    - Use an SFTP client like `WinSCP` (Windows) or `FileZilla` (cross-platform).
    - Connect to your Steam Deck's IP address (found in `System Settings` > `Network`).

## Warpinator

- **Installation**:
    - Install `Warpinator` from the `Discover` store on your Steam Deck.
    - Install `Warpinator` on your PC (available for Linux and Windows).
- **Usage**:
    - Ensure both devices are on the same network.
    - Open `Warpinator` on both devices. They should automatically detect each other.
    - Select the files you want to transfer.

---

# Dependency Management

## ProtonTricks

- **Installation**: Install `ProtonTricks` from the `Discover` store.
- **Usage**:
    - Launch `ProtonTricks`.
    - Select a game to manage its Wine prefix.
    - You can:
        - `Install a Windows DLL or component`.
        - `Run winecfg` to change Wine settings.
        - `Run explorer` to browse the game's C: drive.

---

# Emulation

## EmuDeck

- **Installation**:
    1. Download the `EmuDeck` installer from their website.
    2. Run the installer in Desktop Mode.
    3. Follow the on-screen instructions to configure emulators and paths.
- **Adding ROMs**:
    - Place your ROMs in the `Emulation/roms` folder on your SD card or internal storage.
- **Steam ROM Manager**:
    - EmuDeck uses `Steam ROM Manager` to add emulated games to your Steam library.
    - Run it, and it will automatically generate artwork and shortcuts.

## RetroDeck

- **Installation**: Install `RetroDeck` from the `Discover` store.
- **Configuration**:
    - On first launch, it will create a folder structure for BIOS files and ROMs.
    - Place BIOS files in `~/.var/app/net.retrodeck.retrodeck/data/retrodeck/bios`.
    - Place ROMs in `~/.var/app/net.retrodeck.retrodeck/data/retrodeck/roms`.
- **Adding to Steam**:
    - `RetroDeck` can be added to Steam as a non-Steam game for easy access from Game Mode.

---

# Troubleshooting

- **Game Not Launching**:
    - Try a different Proton version.
    - Check if all dependencies are installed using `ProtonTricks`.
- **Performance Issues**:
    - Lower in-game settings.
    - Use the Steam Deck's built-in performance overlay to monitor FPS and system usage.
- **Controls Not Working**:
    - Use Steam's controller configuration to map controls.
    - For non-Steam games, ensure Steam Input is enabled.

---
</details>
