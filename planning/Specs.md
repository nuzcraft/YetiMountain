# Yeti Mountain Game Specs
## Last Updated: 1/26/2018
### Goal
1.	30-40 minute experience
2.	Turn-based
3.	Grid-based
4.	Ascii + custom tiles
5.	Procedurally Generated
### Tools
1.	Python 2
2.	PyCharm IDE
3.	BearLib Terminal (for output)
4.	Libtcod? (Pathfinding and FOV)
5.	GitHub
6.	RexPaint (Mockups)
7.	Aseprite (art)
8.	Google Docs
### Resource
1.	Drew Erickson
2.	Christian Erickson
### Major Tasks
*	Choose a gameplay theme (ideas below)
    *	Gearing up
        *	Spend time exploring, hunting, and gathering to take down a big boss at the end. 
*	Choose an artistic theme
    *	Outdoors
    *	Weather, season, biome, etc
    *	Underground
    *	Mines, caves, ruins, crystals, etc
    *	Space
    *	Steampunk
    *	Dystopian
    *	Cityscape
*	Build the basic game engine
    *	ECS
*	Add game specific content to engine
    *	Specific tasks should go here
*	Levels and Characters designed around themes and game engine
### Timeline
*	3 Months – Build out basic game engine
*	3 Months – Apply basic character and level development
*	3 Months – Advanced character and level development, advanced UI work
*	3 Months – Polish
*	Total – 12 Months
### Task – Breakout
*	Basic Game Engine
    *	ECS
        *	Start it! Basic entity, component, and system
        *	The easiest system to start with is probably the rendering one.
        *	ETC: 4 hrs
        *   DONE: Actual time: 2.5 hrs
    * Player Loop
        * Craft the basic game loop
        * Render objects, flush to screen, clear objects,  get input, apply changes, repeat 
