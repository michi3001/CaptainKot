# Kotlin Compiler

Dieses Projekt enthält einen einfachen C++-basierten Compiler, der Cap'n Proto-Schemadateien einliest und daraus Kotlin-Interfaces generiert. Der Compiler unterstützt mehrere Datentypen und wandelt sie in die entsprechenden Kotlin-Datentypen um.

## 1. Compiler bauen

Um den Compiler zu bauen, stellen Sie sicher, dass Sie die notwendigen Build-Tools und einen C++17-kompatiblen Compiler (z. B. `g++`) auf Ihrem System installiert haben. Außerdem wird `CMake` zum Erstellen des Build-Systems verwendet.

### Schritte zum Bauen des Compilers

1. **Repository klonen (falls noch nicht vorhanden):**
    ```bash
    git clone https://github.com/michi3001/CaptainKot.git
    cd KotlinCompiler
    ```

2. **Build-Verzeichnis erstellen:**
    ```bash
    mkdir build
    cd build
    ```

3. **CMake ausführen, um das Build-System zu konfigurieren:**
    ```bash
    cmake ..
    ```

4. **Compiler kompilieren:**
     ```bash
    cmake --build .
    ```
    Nach erfolgreichem Bauen wird eine ausführbare Datei (KotlinCompiler.exe) im build-Verzeichnis unter dem Debug Order erstellt.


## 2. Compiler ausführen
Nachdem der Compiler erfolgreich gebaut wurde, kann er genutzt werden, um Cap'n Proto-Schemadateien in Kotlin-Code zu übersetzen.

### Schritte zum Bauen des Compilers
    ```bash
    ./KotlinCompiler <Pfad_zur_Schemadatei>
    ```

    Beispiel:
    ```bash
    ./KotlinCompiler ../schemas/calculator.capnp
    ```
