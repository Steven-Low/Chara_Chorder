; CHORDER
^k::
{
iHook := InputHook("C V","{SPACE}")
iHook.Start()
iHook.Wait()
variable := iHook.Input
variableLength := Strlen(variable)

Loop variableLength + 1
{
	Send "{Backspace}"
}

iHook2 := InputHook("C V","{SPACE}")
iHook2.Start()
iHook2.Wait()
chord := iHook2.Input
chordLength := Strlen(chord)

Loop chordLength + 1
{
	Send "{Backspace}"
}

If (variableLength < 2) || (chordLength < 2)
	return

FileAppend "::" chord "::" variable "`n", A_Desktop "\experiment.ahk"
Reload
}

; CURRENT CHORDS
