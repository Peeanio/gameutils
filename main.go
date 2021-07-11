// Frostgrave warband creator

// Max Russell

package main

import (
	"fmt"
	"math/rand"
	"time"
	"reflect"
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

type PlayerWizards struct {
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

type WizardType struct {
		spell1 string
		spell2 string
		spell3 string
		spell4 string
		spell5 string
		spell6 string
		spell7 string
		spell8 string
		allied1 string
		allied2 string
		allied3 string
		neutral1 string
		neutral2 string
		neutral3 string
		neutral4 string
		neutral5 string
		opposed string

}

var Chronomancer = WizardType{"Crumble", "Decay", "Fast Act", 
	"Fleet Feet", "Petrify", "Slow", "Timestore", "Time Walk", 
	"Necromancer", "Soothsayer", "Elementalist", "Thaumaturge", 
	"Summoner", "Illusionist", "Witch", "Sigilist", "Enchanter"}
	
var Elementalist = WizardType{"Call Storm", "Destructive Sphere",
	"Elemental Ball", "Elemental Bolt", "Elemental Hammer",
	"Elemental Shield", "Scatter Shot", "Wall", "Summoner", 
	"Enchanter", "Chronomancer", "Thaumaturge", "Soothsayer", 
	"Sigilist", "Witch", "Necromancer", "Illusionist"}
	
var Enchanter = WizardType{"Animate Construct", "Control Construct",
	"Embed Enchantment", "Enchant Armour", "Enchant Weapon", "Grenade",
	"Strength", "Telekinesis", "Witch", "Sigilist", "Elementalist",
	"Necromancer", "Illusionist", "Summoner", "Soothsayer", 
	"Thaumaturge", "Chronomancer"}

var Illusionist = WizardType{"Beauty", "Fool's Gold", "Glow", 
	"Illusionary Solider", "Invisibility", "Monstrous Form", "Teleport",
	"Transpose", "Soothsayer", "Sigilist", "Thaumaturge", "Necromancer",
	"Witch", "Chronomancer", "Summoner", "Enchanter", "Elementalist"}
	
var Necromancer = WizardType{"Bone Dart", "Bones of the Earth", 
	"Control Undead", "Raise Zombie", "Reveal Death", "Spell Eater",
	"Steal Health", "Strike Dead", "Witch", "Chronomancer", "Summoner",
	"Elementalist", "Sigilist", "Illusionist", "Enchanter", 
	"Soothsayer", "Thaumaturge"}

var Sigilist = WizardType{"Absorb Knowledge", "Create Grimoire", 
	"Draining Word", "Explosive Rune", "Furious Quill", "Power Word",
	"Push", "Write Scroll", "Thaumaturge", "Illusionist", "Enchanter",
	"Necromancer", "Elementalist", "Witch", "Chronomancer", 
	"Soothsayer", "Summoner"}
	
var Soothsayer = WizardType{"Awareness", "Combat Awareness", 
	"Forget Spell", "Mind Control", "Reveal Invisible", "Reveal Secret",
	"Will Power", "Wizard Eye", "Thaumaturge", "Chronomancer", 
	"Illusionist", "Enchanter", "Summoner", "Necromancer", 
	"Elementalist", "Sigilist", "Witch"}
	
var Summoner = WizardType{"Bind Demon", "Imp", "Leap", 
	"Plague of Insects", "Planar Tear", "Planar Walk","Possess", 
	"Summon Demon", "Necromancer", "Witch", "Elementalist", 
	"Soothsayer", "Enchanter", "Illusionist", "Chronomancer", 
	"Thaumaturge", "Sigilist"}
	
var Thaumaturge = WizardType{"Banish", "Blinding Light", 
	"Circle of Protection", "Dispel", "Heal", "Miraculus Cure",
	"Restore Life", "Shield", "Soothsayer", "Sigilist", "Illusionist",
	"Elementalist", "Witch", "Chronomancer", "Summoner", "Enchanter",
	"Necromancer"}
	
	
var Witch = WizardType{"Animal Companion", "Brew Potion", 
	"Control Animal", "Curse", "Familiar", "Fog", "Mud", "Posion Dart",
	"Enchanter", "Necromancer", "Summoner", "Thaumaturge", 
	"Illusionist", "Elementalist", "Sigilist", "Chronomancer", 
	"Soothsayer"}

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

var startingGold = 500

func returnSpell(x WizardType) reflect.Value{
		var s reflect.Value
		switch x {
		case Chronomancer: 
			w := reflect.ValueOf(&Chronomancer).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Elementalist: 
			w := reflect.ValueOf(&Elementalist).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Enchanter: 
			w := reflect.ValueOf(&Enchanter).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Illusionist: 
			w := reflect.ValueOf(&Illusionist).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Necromancer: 
			w := reflect.ValueOf(&Necromancer).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Sigilist: 
			w := reflect.ValueOf(&Sigilist).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Soothsayer: 
			w := reflect.ValueOf(&Soothsayer).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Summoner: 
			w := reflect.ValueOf(&Summoner).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Thaumaturge: 
			w := reflect.ValueOf(&Thaumaturge).Elem()
			s:= w.Field(rollTox(8))
			return(s)
		case Witch: 
			w := reflect.ValueOf(&Witch).Elem()
			s:= w.Field(rollTox(8))
			return(s)
			//			fmt.Println(w.Field(rollTox(8)))
	}
	return(s)
}

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

	
	//currentGold := startingGold

	//soldierSlice := make([]string, 0)

//	playerKnownSpells := make([]string, 8)
	playerWizardType := wizardTypeArray[rollTox(10)]
	fmt.Println("Wizard type is", playerWizardType)
	fmt.Println("Starting Gold: ", startingGold)
	fmt.Println(soldiersCostMap[soliderNumberArray[rollTox(15)]])
    //fmt.Println((`playerWizardType`).opposed) // why doesn't this work?	
	switch playerWizardType {
		case "Chronomancer": fmt.Println(Chronomancer.opposed)
		case "Elementalist": fmt.Println(Elementalist.opposed)
		case "Enchanter": fmt.Println(Enchanter.opposed)
		case "Illusionist": fmt.Println(Illusionist.opposed)
		case "Necromancer": fmt.Println(Necromancer.opposed)
		case "Sigilist": fmt.Println(Sigilist.opposed)
		case "Soothsayer": fmt.Println(Soothsayer.opposed)
		case "Summoner": fmt.Println(Summoner.opposed)
		case "Thaumaturge": fmt.Println(Thaumaturge.opposed)
		case "Witch": fmt.Println(Witch.opposed)
	}
	//slice :=  make([]reflect.Value, 0, 8 )
	
	//i := 1
	//for i <= 3 {
		//playerSpellSlice := append(slice, returnSpell(Witch))
		//fmt.Println(i)
		//i = i + 1
	//}
	
	//fmt.Println(playerSpellSlice)
	fmt.Println("First spell is: ", returnSpell(Witch))

}
