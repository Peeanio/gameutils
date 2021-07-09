// Frostgrave warband creator

// Max Russell

package main

import (
	"fmt"
	"math/rand"
	"time"
//	"strconv"
)

//spells: three own school, one each aligned, two neautral (different)

//stats: move (m) fight (f) shoot (s) armour (a) will (w) health (h)
//starting wizard: 6 +2 +0 10 +4 14

//start w/ 500gc
//200gc apprentice
// 6 w-2 w-2 10 w-2 w-4
// 6 +0 -2 10 +2 10

type Soldiers struct {
		name string
		cost int
}

type Wizards struct {
		school string
		spell1 string
		spell2 string
		spell3 string
		spell4 string
		spell5 string
		spell6 string
		spell7 string
		spell8 string
}

//Following are various arrays, which are also held with blank identifers
var chronomancerSpells = [8]string{
		"Crumble",
		"Decay",
		"Fast Act",
		"Fleet Feet",
		"Petrify",
		"Slow",
		"Timestore",
		"Time Walk",
}

var elementalistSpells = [8]string{
		"Call Storm",
		"Destructive Sphere",
		"Elemental Ball",
		"Elemental Bolt",
		"Elemental Hammer",
		"Elemental Shield",
		"Scatter Shot",
		"Wall",
	}


var enchanterSpells = [8]string{
		"Animate Construct",
		"Control Construct",
		"Embed Enchantment",
		"Enchant Armour",
		"Enchant Weapon",
		"Grenade",
		"Strength",
		"Telekinesis",
	}


var illusionistSpells = [8]string{
		"Beauty",
		"Fool's Gold",
		"Glow",
		"Illusionary Solider",
		"Invisibility",
		"Monstrous Form",
		"Teleport",
		"Transpose",
	}


var	necromancerSpells = [8]string{
		"Bone Dart",
		"Bones of the Earth",
		"Control Undead",
		"Raise Zombie",
		"Reveal Death",
		"Spell Eater",
		"Steal Health",
		"Strike Dead",
	}


var	sigilistSpells = [8]string{
		"Absorb Knowledge",
		"Create Grimoire",
		"Draining Word",
		"Explosive Rune",
		"Furious Quill",
		"Power Word",
		"Push",
		"Write Scroll",
	}


var	soothsayerSpells = [8]string{
		"Awareness",
		"Combat Awareness",
		"Forget Spell",
		"Mind Control",
		"Reveal Invisible",
		"Reveal Secret",
		"Will Power",
		"Wizard Eye",
	}


var	summonerSpells = [8]string{
		"Bind Demon",
		"Imp",
		"Leap",
		"Plague of Insects",
		"Planar Tear",
		"Possess",
		"Summon Demon",
	}


var	thaumaturgeSpells = [8]string{
		"Banish",
		"Blinding Light",
		"Circle of Protection",
		"Dispel",
		"Heal",
		"Miraculous Cure",
		"Restore Life",
		"Shield",
	}


var	witchSpells = [8]string{
		"Animal Companion",
		"Brew Potion",
		"Control Animal",
		"Curse",
		"Familiar",
		"Fog",
		"Mud",
		"Posion Dart",
	}


var	soldiersCostMap = map[string]int{
		"War Hound": 20,
		"Thug": 20,
		"Archer": 50,
		"Crossbowman": 50,
		"Infantryman": 50,
		"Tracker": 80,
		"Man-at-Arms": 80,
		"Treasure Hunter": 80,
		"Knight": 100,
		"Templar": 100,
		"Ranger": 100,
		"Barbarian": 100,
		"Apothecary": 100,
		"Marksman": 100,
		"Apprentice": 200,
	}

var	soliderNumberArray = [15]string{
		"War Hound",
		"Thug",
		"Archer",
		"Crossbowman",
		"Infantryman",
		"Tracker",
		"Man-at-Arms",
		"Treasure Hunter",
		"Knight",
		"Templar",
		"Ranger",
		"Barbarian",
		"Apothecary",
		"Marksman",
		"Apprentice",
	}

var	wizardTypeArray = [10]string{
		"Chronomancer",
		"Elementalist",
		"Enchanter",
		"Illusionist",
		"Necromancer",
		"Sigilist",
		"Soothsayer",
		"Summoner",
		"Thaumaturge",
		"Witch",
	}

var	chronomancerAllied = [3]string{
		"Necromancer",
		"Soothsayer",
		"Elementalist",
	}


var	chronomancerNeutral = [5]string {
		"Thaumaturge",
		"Summoner",
		"Illusionist",
		"Witch",
		"Sigilist",
	}


var	elementalistAllied = [3]string{
		"Summoner",
		"Enchanter",
		"Chronomancer",
	}


var	elementalistNeutral = [5]string {
		"Thaumaturge",
		"Soothsayer",
		"Sigilist",
		"Witch",
		"Necromancer",
	}


var	enchanterAllied = [3]string{
		"Witch",
		"Sigilist",
		"Elementalist",
	}


var	enchanterNeutral = [5]string {
		"Witch",
		"Illusionist",
		"Summoner",
		"Soothsayer",
		"Thaumaturge",
	}


var	illusionistAllied = [3]string{
		"Soothsayer",
		"Sigilist",
		"Thaumaturge",
	}


var	illusionistNeutral = [5]string {
		"Necromancer",
		"Witch",
		"Chronomancer",
		"Summoner",
		"Enchanter",
	}


var	necromancerAllied = [3]string{
		"Witch",
		"Chronomancer",
		"Summoner",
	}


var	necromancerNeutral = [5]string{
		"Elementalist",
		"Sigilist",
		"Illusionist",
		"Enchanter",
		"Soothsayer",
	}


var	sigilistAllied = [3]string{
		"Thaumaturge",
		"Illusionist",
		"Enchanter",
	}


var	sigilistNeutral = [5]string{
		"Necromancer",
		"Elementalist",
		"Witch",
		"Chronomancer",
		"Soothsayer",
	}


var	soothsayerAllied = [3]string{
		"Thaumaturge",
		"Chronomancer",
		"Illusionist",
	}


var	soothsayerNeutral = [5]string{
		"Enchanter",
		"Summoner",
		"Necromancer",
		"Elementalist",
		"Sigilist",
	}


var	summonerAllied = [3]string{
		"Necromancer",
		"Witch",
		"Elementalist",
	}


var	summonerNeutral = [5]string{
		"Soothsayer",
		"Enchanter",
		"Illusionist",
		"Chronomancer",
		"Thaumaturge",
	}


var	thaumaturgeAllied = [3]string{
		"Soothsayer",
		"Sigilist",
		"Illusionist",
	}


var	thaumaturgeNeutral = [5]string{
		"Elementalist",
		"Witch",
		"Chronomancer",
		"Summoner",
		"Enchanter",
	}


var	witchAllied = [3]string{
		"Enchanter",
		"Necromancer",
		"Summoner",
	}


var	witchNeutral = [5]string{
		"Thaumaturge",
		"Illusionist",
		"Elementalist",
		"Sigilist",
		"Chronomancer",
	}


var	opposedMap = map[string]string{
		"Chronomancer" : "Enchanter",
		"Elementalist" : "Illusionist",
		"Enchanter" : "Chronomancer",
		"Illusionist" : "Elementalist",
		"Necromancer" : "Thaumaturge",
		"Sigilist" : "Summoner",
		"Soothsayer" : "Witch",
		"Summoner" : "Sigilist",
		"Thaumaturge" : "Necromancer",
		"Witch" : "Soothsayer",
	}

var startingGold = 500

func rollDx(x int) int {
//rolls a die up to the number specified
	min := 1
	max := x + 1
	return rand.Intn(max - min) + min

}

func rollTox(x int) int {
//rolls from zero to number specified
	return rand.Intn(x)
}

//func addSolider(currentGold int, soliderNumberArray ) int {
//passes in remaining gold, returns the solider bought and remaining money
//	newSoldier := soliderNumberArray[rollTox(15)]
//	if (currentGold - soldierCostMap[newSolider]) >= 0 {
//		curentGold = ( currentGold - soldierCostMap[newSoldier])
//		soldierSlice := append(newSoldier)
//	} else {
//	}
//}

func main() {
	rand.Seed(time.Now().UnixNano())

	
	currentGold := startingGold

	soldierSlice := make([]string, 0)

//	playerKnownSpells := make([]string, 8)
	playerWizardType := wizardTypeArray[rollTox(10)]

	fmt.Println("Wizard type is", playerWizardType)
	fmt.Println("Starting Gold: ", startingGold)
	fmt.Println(soldiersCostMap[soliderNumberArray[rollTox(15)]])
	fmt.Println(opposedMap[playerWizardType])
}
