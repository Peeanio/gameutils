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
	fmt.Println(rollDx(10))
	startingGold := 500

	type Soldiers struct {
		name string
		cost int
	
	}

	type Wizards struct {
		school string
		
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
	fmt.Println(startingGold)
	fmt.Println(soldiersCostMap["Archer"])
}
