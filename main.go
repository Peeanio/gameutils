// Frostgrave warband creator

// Max Russell

package main

import (
	"fmt"
	"math/rand"
	"time"
//	"strconv"
)

//classes w/ oposition
//chronomancer 
//  +2 necro sooth ele
//  +4 tha summ ill witch sigil
//  +6 enchant

//elementalist
//  +2 summ en chr
//  +4 tha sooth sig wit nec
//  +6 ill

//enchanter
//  +2 wit sigil ele
//  +4 nec ill sum sooth tha
//  +6 chrono

//illusionist
//  +2 sooth sigil tha
//  +4 nec wit chro summ enc
//  +6 ele

//necromancer
//  +2 wit chro summ
//  +4 ele sig ill enc soot
//  +6 tha

//sigilist
//  +2 tha ill enc
//  +4 nec ele wit chro soo
//  +6 summ

//soothsayer
//  +2 tha chro ill
//  +4 ench summ necr ele sigil
//  +6 witch

//summoner
//  +2 necro witch ele
//  +4 sooth enc ill chro tha
//  +6 sigi

//thaumaturge
//  +2 soot sigil ill
//  +4 ele witch chro summ ench
//  +6 necro

//witch
//  +2 enc necr summ
//  +4 tha ill ele sigi chro
//  +6 soot

//spells: three own school, one each aligned, two neautral (different)

//stats: move (m) fight (f) shoot (s) armour (a) will (w) health (h)
//starting wizard: 6 +2 +0 10 +4 14

//start w/ 500gc
//200gc apprentice
// 6 w-2 w-2 10 w-2 w-4
// 6 +0 -2 10 +2 10

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

func main() {
	rand.Seed(time.Now().UnixNano())
	startingGold := 500

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

	chronomancerSpells := [8]string{
		"Crumble",
		"Decay",
		"Fast Act",
		"Fleet Feet",
		"Petrify",
		"Slow",
		"Timestore",
		"Time Walk",
	}

	elementalistSpells := [8]string{
		"Call Storm",
		"Destructive Sphere",
		"Elemental Ball",
		"Elemental Bolt",
		"Elemental Hammer",
		"Elemental Shield",
		"Scatter Shot",
		"Wall",
	}

	enchanterSpells := [8]string{
		"Animate Construct",
		"Control Construct",
		"Embed Enchantment",
		"Enchant Armour",
		"Enchant Weapon",
		"Grenade",
		"Strength",
		"Telekinesis",
	}

	illusionistSpells := [8]string{
		"Beauty",
		"Fool's Gold",
		"Glow",
		"Illusionary Solider",
		"Invisibility",
		"Monstrous Form",
		"Teleport",
		"Transpose",
	}

	necromancerSpells := [8]string{
		"Bone Dart",
		"Bones of the Earth",
		"Control Undead",
		"Raise Zombie",
		"Reveal Death",
		"Spell Eater",
		"Steal Health",
		"Strike Dead",
	}

	sigilistSpells := [8]string{
		"Absorb Knowledge",
		"Create Grimoire",
		"Draining Word",
		"Explosive Rune",
		"Furious Quill",
		"Power Word",
		"Push",
		"Write Scroll",
	}

	soothsayerSpells := [8]string{
		"Awareness",
		"Combat Awareness",
		"Forget Spell",
		"Mind Control",
		"Reveal Invisible",
		"Reveal Secret",
		"Will Power",
		"Wizard Eye",
	}

	summonerSpells := [8]string{
		"Bind Demon",
		"Imp",
		"Leap",
		"Plague of Insects",
		"Planar Tear",
		"Possess",
		"Summon Demon",
	}

	thaumaturgeSpells := [8]string{
		"Banish",
		"Blinding Light",
		"Circle of Protection",
		"Dispel",
		"Heal",
		"Miraculous Cure",
		"Restore Life",
		"Shield",
	}

	witchSpells := [8]string{
		"Animal Companion",
		"Brew Potion",
		"Control Animal",
		"Curse",
		"Familiar",
		"Fog",
		"Mud",
		"Posion Dart",
	}

	soldiersCostMap := map[string]int{
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

	soliderNumberArray := [15]string{
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

	wizardTypeArray := [10]string{
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

//	playerKnownSpells := make([]string, 8)


	playerWizardType := wizardTypeArray[rollTox(10)]

	fmt.Println(playerWizardType)
	fmt.Println("Starting Gold: ", startingGold)
	fmt.Println(soldiersCostMap[soliderNumberArray[rollTox(15)]])
	fmt.Println(witchSpells[rollTox(8)])
	fmt.Println(thaumaturgeSpells[rollTox(8)])
	fmt.Println(enchanterSpells[rollTox(8)])
	fmt.Println(chronomancerSpells[rollTox(8)])
	fmt.Println(elementalistSpells[rollTox(8)])
	fmt.Println(illusionistSpells[rollTox(8)])
	fmt.Println(necromancerSpells[rollTox(8)])
	fmt.Println(sigilistSpells[rollTox(8)])
	fmt.Println(soothsayerSpells[rollTox(8)])
	fmt.Println(summonerSpells[rollTox(8)])

}
