Description
----------------
This Python script adeptly transforms Minecraft NBT structure
files into JSON, tailors the JSON content using criteria from
`searchterms.txt` and `replacements.txt`, and then meticulously
reconverts the JSON back into NBT format for seamless Minecraft integration.

Requirements
----------------
* python - `3.8`
* nbtlib - `1.12.1`

Step by step
----------------
1. Input blocks you want to replace into searchterms.txt
2. Add blocks youre replacing to replacements.txt


    NOTE : The 2 txt files are direct line for line replacements,
            what ever is on line 69 in searchterms.txt is replaced
            by line 69 in replacements.txt 

3. Open `path.py` and add the path to the structures folder you want to modify,
   
   E.G. - "B:\Modded Minecraft\instances\FirmaLand2\kubejs\data\dungeons_arise\structures"
    
    This path is directly copied from Windows File Explorer


4. Install `python 3.8` or higher
5. Install specifically this verion of nbtLib `pip install "nbtlib==1.12.1"`
6. Enter command `python .\fullProcess.py` to run all scripts and automatically alter all the nbt files in the directory/sub directories

