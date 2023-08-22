"""
Filename: data.py
Author: Josh Patterson
Date: 8/21/2023

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

This file contains the necessary data structures for logic.py
"""

KONTAKT_TO_REAPER = {
    'C-2': 'C-1', 'C#-2': 'C#-1', 'D-2': 'D-1', 'D#-2': 'D#-1', 'E-2': 'E-1', 'F-2': 'F-1', 'F#-2': 'F#-1',
    'G-2': 'G-1', 'G#-2': 'G#-1', 'A-2': 'A-1', 'A#-2': 'A#-1', 'B-2': 'B-1', 'C-1': 'C0', 'C#-1': 'C#0',
    'D-1': 'D0', 'D#-1': 'D#0', 'E-1': 'E0', 'F-1': 'F0', 'F#-1': 'F#0', 'G-1': 'G0', 'G#-1': 'G#0',
    'A-1': 'A0', 'A#-1': 'A#0', 'B-1': 'B0', 'C0': 'C1', 'C#0': 'C#1', 'D0': 'D1', 'D#0': 'D#1',
    'E0': 'E1', 'F0': 'F1', 'F#0': 'F#1', 'G0': 'G1', 'G#0': 'G#1', 'A0': 'A1', 'A#0': 'A#1',
    'B0': 'B1', 'C1': 'C2', 'C#1': 'C#2', 'D1': 'D2', 'D#1': 'D#2', 'E1': 'E2', 'F1': 'F2',
    'F#1': 'F#2', 'G1': 'G2', 'G#1': 'G#2', 'A1': 'A2', 'A#1': 'A#2', 'B1': 'B2', 'C2': 'C3',
    'C#2': 'C#3', 'D2': 'D3', 'D#2': 'D#3', 'E2': 'E3', 'F2': 'F3', 'F#2': 'F#3', 'G2': 'G3',
    'G#2': 'G#3', 'A2': 'A3', 'A#2': 'A#3', 'B2': 'B3', 'C3': 'C4', 'C#3': 'C#4', 'D3': 'D4',
    'D#3': 'D#4', 'E3': 'E4', 'F3': 'F4', 'F#3': 'F#4', 'G3': 'G4', 'G#3': 'G#4', 'A3': 'A4',
    'A#3': 'A#4', 'B3': 'B4', 'C4': 'C5', 'C#4': 'C#5', 'D4': 'D5', 'D#4': 'D#5', 'E4': 'E5',
    'F4': 'F5', 'F#4': 'F#5', 'G4': 'G5', 'G#4': 'G#5', 'A4': 'A5', 'A#4': 'A#5', 'B4': 'B5',
    'C5': 'C6', 'C#5': 'C#6', 'D5': 'D6', 'D#5': 'D#6', 'E5': 'E6', 'F5': 'F6', 'F#5': 'F#6',
    'G5': 'G6', 'G#5': 'G#6', 'A5': 'A6', 'A#5': 'A#6', 'B5': 'B6', 'C6': 'C7', 'C#6': 'C#7',
    'D6': 'D7', 'D#6': 'D#7', 'E6': 'E7', 'F6': 'F7', 'F#6': 'F#7', 'G6': 'G7', 'G#6': 'G#7',
    'A6': 'A7', 'A#6': 'A#7', 'B6': 'B7', 'C7': 'C8', 'C#7': 'C#8', 'D7': 'D8', 'D#7': 'D#8',
    'E7': 'E8', 'F7': 'F8', 'F#7': 'F#8', 'G7': 'G8', 'G#7': 'G#8', 'A7': 'A8', 'A#7': 'A#8',
    'B7': 'B8', 'C8': 'C9', 'C#8': 'C#9', 'D8': 'D9', 'D#8': 'D#9', 'E8': 'E9', 'F8': 'F9',
    'G8': 'F#9'
}

REAPER_MIDI_NOTE_MAP = {
    'C-1': '0', 'C#-1': '1', 'D-1': '2', 'D#-1': '3', 'E-1': '4', 'F-1': '5', 'F#-1': '6', 'G-1': '7',
    'G#-1': '8', 'A-1': '9', 'A#-1': '10', 'B-1': '11', 'C0': '12', 'C#0': '13', 'D0': '14', 'D#0': '15',
    'E0': '16', 'F0': '17', 'F#0': '18', 'G0': '19', 'G#0': '20', 'A0': '21', 'A#0': '22', 'B0': '23',
    'C1': '24', 'C#1': '25', 'D1': '26', 'D#1': '27', 'E1': '28', 'F1': '29', 'F#1': '30', 'G1': '31',
    'G#1': '32', 'A1': '33', 'A#1': '34', 'B1': '35', 'C2': '36', 'C#2': '37', 'D2': '38', 'D#2': '39',
    'E2': '40', 'F2': '41', 'F#2': '42', 'G2': '43', 'G#2': '44', 'A2': '45', 'A#2': '46', 'B2': '47',
    'C3': '48', 'C#3': '49', 'D3': '50', 'D#3': '51', 'E3': '52', 'F3': '53', 'F#3': '54', 'G3': '55',
    'G#3': '56', 'A3': '57', 'A#3': '58', 'B3': '59', 'C4': '60', 'C#4': '61', 'D4': '62', 'D#4': '63',
    'E4': '64', 'F4': '65', 'F#4': '66', 'G4': '67', 'G#4': '68', 'A4': '69', 'A#4': '70', 'B4': '71',
    'C5': '72', 'C#5': '73', 'D5': '74', 'D#5': '75', 'E5': '76', 'F5': '77', 'F#5': '78', 'G5': '79',
    'G#5': '80', 'A5': '81', 'A#5': '82', 'B5': '83', 'C6': '84', 'C#6': '85', 'D6': '86', 'D#6': '87',
    'E6': '88', 'F6': '89', 'F#6': '90', 'G6': '91', 'G#6': '92', 'A6': '93', 'A#6': '94', 'B6': '95',
    'C7': '96', 'C#7': '97', 'D7': '98', 'D#7': '99', 'E7': '100', 'F7': '101', 'F#7': '102', 'G7': '103',
    'G#7': '104', 'A7': '105', 'A#7': '106', 'B7': '107', 'C8': '108', 'C#8': '109', 'D8': '110', 'D#8': '111',
    'E8': '112', 'F8': '113', 'F#8': '114', 'G8': '115', 'G#8': '116', 'A8': '117', 'A#8': '118', 'B8': '119',
    'C9': '120', 'C#9': '121', 'D9': '122', 'D#9': '123', 'E9': '124', 'F9': '125', 'F#9': '126', 'G9': '127'
}


def convert_kontakt_note_to_reaper_note(note):
    # This function is here because MIDI notes in Kontakt do not directly correspond to notes in Reaper
    # C-2 in Kontakt corresponds to a C-1 in Reaper (everything is one octave up in Reaper)
    # Also Kontakt skips F#8 for some reason
    return KONTAKT_TO_REAPER[note]
def get_number_from_note(note):
    # This function tells you what number in Reaper's piano roll (0-127) a note corresponds to
    return int(REAPER_MIDI_NOTE_MAP[note])

KONTAKT_NOTES = [
    'C-2', 'C#-2', 'D-2', 'D#-2', 'E-2', 'F-2', 'F#-2', 'G-2', 'G#-2', 'A-2', 'A#-2', 'B-2', 'C-1', 'C#-1',
    'D-1', 'D#-1', 'E-1', 'F-1', 'F#-1', 'G-1', 'G#-1', 'A-1', 'A#-1', 'B-1', 'C0', 'C#0', 'D0', 'D#0', 'E0',
    'F0', 'F#0', 'G0', 'G#0', 'A0', 'A#0', 'B0', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1',
    'A1', 'A#1', 'B1', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3',
    'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4',
    'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5',
    'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 'C7', 'C#7', 'D7', 'D#7', 'E7',
    'F7', 'G7', 'G#7', 'A7', 'A#7', 'B7', 'C8', 'C#8', 'D8', 'D#8', 'E8', 'F8', 'G8'
]


# arrays of in-order (left-to-right column based) articulation names
# the index i of each kit piece, when compared to the .nka file, tells us which line number that kit piece
# corresponds to in the .nka file
# for example, if line number 3 in the .nka file equals 0, that means it corresponds to TEXT_LIST[0]

INVASION_TEXT = [
    'Left', 'Right', 'Auto Double Kick', 'Hit', 'Flam', 'Wires Off', 'Ruft', 'Sidestick', 'Rack Tom 1 Hit',
    'Rack Tom 2 Hit', 'Rack Tom 3 Hit', 'Floor Tom 1 Hit', 'Floor Tom 2 Hit', 'Floor Tom 3 Hit', 'Main Crash L Hit',
    'Main Crash L Choke', 'Wide Crash L Hit', 'Wide Crash L Choke', 'Main Crash R Hit', 'Main Crash R Choke',
    'Wide Crash R Hit', 'Wide Crash R Choke', 'China L Hit', 'China L Choke ', 'China R Hit', 'China R Choke',
    'Bell', 'Rate', 'Edge', 'Tip Tight', 'Edge Tight', 'Tip Closed', 'Eye Closed', 'Open 1', 'Open 2', 'Open 3',
    'Peal', 'CC', 'Xhat Closed', 'Xhat Open', 'Splash L Hit', 'Splash L Choke', 'Splash C Hit', 'Splash C Choke',
    'Stack Hit', 'Bell L Hit', 'Bell R: Ht'
]

OKW_AGGRESSIVE_ROCK_TEXT = [
    'Kick', 'Snare Hit', 'Cross Stick', 'Tom 1: Hit', 'Tom 2: Hit', 'Tip Tight', 'Edge Tight', 'Tip Closed',
    'Ede Closed:', 'Open 1', 'Open 2', 'Open 3', 'Pedal', 'CC', 'Bell', 'Bow', 'Crash L Hit', 'Crash L Choke',
    'Crash R Hit', 'Crash R Choke', 'Splash Hit', 'Splash Choke', 'China Hit', 'China Choke'
]

OKW_ARCHITECTS_TEXT = [
    'Kick', 'Snare Hit', 'Cross Stick', 'Tom 1 Hit', 'Tom 2 Hit', 'Tom 3 Hit', 'Ride Bell', 'Ride Bow', 'Ride Crash',
    'Ride Choke', 'Main L Hit', 'Main L Choke', 'Main R Hit', 'Main R Choke', 'Wide R Hit', 'Wide R Choke', 'Tip Tight',
    'Edge Tight', 'Tip Closed', 'Edge Closed', 'Open 1', 'Open 2', 'Open 3', 'Pedal', 'CC', 'China Hit', 'China Choke',
    'Splash Hit', 'Splash Choke', 'Mini China Hit', 'Mini China Choke', 'X-hat Hit'
]

OKW_METAL_TEXT = [
    'Left', 'Right', 'Double Kick', 'Hit', 'Cross Stick', 'Tip Tight', 'Edge Tight', 'Tip Closed', 'Edge Closed',
    'Open 1', 'Open 2', 'Open 3', 'Pedal', 'CC', 'Ride Bell', 'Ride Bow', 'Tom 1: Hit', 'Tom 2: Hit', 'Tom 3: Hit',
    'Tom 4: Hit', 'Left Hit', 'Left Choke', 'Center Hit', 'Center Choke', 'Right Hit', 'Right Choke', 'China Hit',
    'China Choke', 'Splash Lefts Hit', 'Splash Left Choke', 'Splash Center Hit', 'Splash Center Choke'
]

P4_HALPERN_TEXT = [
    'Kick', 'Snare Hit', 'Snare Flam', 'Wires Off', 'Ruft', 'Sidestick', 'Rack Tom 1 Hit', 'Rack Tom 2 Hit',
    'Floor Tom 1 Hit', 'Floor Tom 1 Hit', 'Stick Click', 'Tip Tight', 'Edge Tight', 'Tip Closed', 'Edge Closed',
    'Open 1', 'Open 2', 'Open 3', 'Pedal', 'Pedal Chink', 'CC', 'Ride Bell', 'Ride Bow', 'China Hit', 'China Choke',
    'Main Crash L Hit', 'Main Crash L Choke', 'Wide Crash L Hit', 'Wide Crash L Choke', 'Main Crash R Hit',
    'Main Crash L Hit', 'Splash L Hit', 'Splash L Choke', 'Splash C Hit', 'Splash C Choke', 'Mini Hats Hit', 'Stack Hit'
]

HALPERN_ORIGINAL_TEXT = [
    'Kick Main Hit', 'Stick Click Kick Hit', 'Snare Hit', 'Flam', 'Ruff', 'Snare-Off', 'Stick Click', 'Hi Tom Hit',
    'Hi Tom Rim Hit', 'Mid Tom 1 Main Hit', 'Mid Tom 1 Rim Hit', 'Mid Tom 2 Main Hit', 'Mid Tom 2 Rim Hit', 'Floor Tom Main Hit',
    'Floor Tom Rim Hit', 'Pedal Chik', 'Pedal Ching', 'Tip Tight', 'Edge Tight', 'Tip Closed', 'Edge Closed', 'Tip Loose',
    'Edge Loose', 'Tip Open 1', 'Edge Open 1', 'Tip Open 2', 'Edge Open 2', 'Tip Open 3', 'Edge Open 3', 'Tip Wide', 'Edge Wide',
    'Hi Hat CC', 'Left Crash Hit', 'Left Crash Bell', 'Left Crash Choke', 'Left Crash Swell', 'Right Crash Hit', 'Right Crash Bell',
    'Right Crash Choke', 'Right Crash Swell', 'Ride Tip', 'Ride Crash', 'Ride Bell Tip', 'Ride Bell Shoulder', 'China Main Hit',
    'China Choke', 'Stack Tight Hit', 'Stack Loose Hit', 'Splash Hit'
]

# LOGIC FOR DETERMINING WHICH LINE NUMBER IN AN NKA FILE EACH KIT PIECE CORRESPONDS TO
#
# with open('C:/Dev/Projects/PyCharm/ReaperMidiNoteNameGen/resources/NKAFiles/SequentiallyOrdered/P4MattHalpern.nka', 'r') as f:
#     lst = f.read().splitlines()
#
#     for kit_piece_idx, piece in enumerate(P4_HALPERN_TEXT):
#         line_number = lst.index(str(kit_piece_idx))
#         p4_nka[piece] = line_number
#
#     print(p4_nka)

invasion_nka = {'Left': 2, 'Right': 3, 'Auto Double Kick': 4, 'Hit': 6, 'Flam': 5, 'Wires Off': 9, 'Ruft': 7,
                'Sidestick': 8, 'Rack Tom 1 Hit': 10, 'Rack Tom 2 Hit': 11, 'Rack Tom 3 Hit': 12, 'Floor Tom 1 Hit': 13,
                'Floor Tom 2 Hit': 14, 'Floor Tom 3 Hit': 15, 'Main Crash L Hit': 33, 'Main Crash L Choke': 32,
                'Wide Crash L Hit': 31, 'Wide Crash L Choke': 30, 'Main Crash R Hit': 37, 'Main Crash R Choke': 36,
                'Wide Crash R Hit': 35, 'Wide Crash R Choke': 34, 'China L Hit': 39, 'China L Choke ': 38, 'China R Hit': 41,
                'China R Choke': 40, 'Bell': 27, 'Rate': 29, 'Edge': 28, 'Tip Tight': 23, 'Edge Tight': 22, 'Tip Closed': 17,
                'Eye Closed': 16, 'Open 1': 18, 'Open 2': 19, 'Open 3': 20, 'Peal': 21, 'CC': 24, 'Xhat Closed': 25,
                'Xhat Open': 26, 'Splash L Hit': 43, 'Splash L Choke': 42, 'Splash C Hit': 45, 'Splash C Choke': 44,
                'Stack Hit': 48, 'Bell L Hit': 46, 'Bell R: Ht': 47}

aggressive_rock_nka = {'Kick': 2, 'Snare Hit': 4, 'Cross Stick': 3, 'Tom 1: Hit': 5, 'Tom 2: Hit': 6, 'Tip Tight': 14,
                       'Edge Tight': 13, 'Tip Closed': 8, 'Ede Closed:': 7, 'Open 1': 9, 'Open 2': 10, 'Open 3': 11,
                       'Pedal': 12, 'CC': 15, 'Bell': 16, 'Bow': 17, 'Crash L Hit': 19, 'Crash L Choke': 18, 'Crash R Hit': 21,
                       'Crash R Choke': 20, 'Splash Hit': 25, 'Splash Choke': 24, 'China Hit': 23, 'China Choke': 22}

architects_nka = {'Kick': 2, 'Snare Hit': 4, 'Cross Stick': 3, 'Tom 1 Hit': 6, 'Tom 2 Hit': 7, 'Tom 3 Hit': 8, 'Ride Bell': 18,
                  'Ride Bow': 19, 'Ride Crash': 20, 'Ride Choke': 34, 'Main L Hit': 22, 'Main L Choke': 21, 'Main R Hit': 24,
                  'Main R Choke': 23, 'Wide R Hit': 26, 'Wide R Choke': 25, 'Tip Tight': 16, 'Edge Tight': 15, 'Tip Closed': 10,
                  'Edge Closed': 9, 'Open 1': 11, 'Open 2': 12, 'Open 3': 13, 'Pedal': 14, 'CC': 17, 'China Hit': 33, 'China Choke': 32,
                  'Splash Hit': 30, 'Splash Choke': 29, 'Mini China Hit': 28, 'Mini China Choke': 27, 'X-hat Hit': 159}

metal_nka = {'Left': 2, 'Right': 3, 'Double Kick': 4, 'Hit': 6, 'Cross Stick': 5, 'Tip Tight': 18, 'Edge Tight': 17,
             'Tip Closed': 12, 'Edge Closed': 11, 'Open 1': 13, 'Open 2': 14, 'Open 3': 15, 'Pedal': 16, 'CC': 19,
             'Ride Bell': 20, 'Ride Bow': 21, 'Tom 1: Hit': 7, 'Tom 2: Hit': 8, 'Tom 3: Hit': 9, 'Tom 4: Hit': 10,
             'Left Hit': 23, 'Left Choke': 22, 'Center Hit': 25, 'Center Choke': 24, 'Right Hit': 27, 'Right Choke': 26,
             'China Hit': 29, 'China Choke': 28, 'Splash Lefts Hit': 31, 'Splash Left Choke': 30, 'Splash Center Hit': 33,
             'Splash Center Choke': 32}

p4_nka = {'Kick': 2, 'Snare Hit': 5, 'Snare Flam': 4, 'Wires Off': 7, 'Ruft': 6, 'Sidestick': 3, 'Rack Tom 1 Hit': 8,
          'Rack Tom 2 Hit': 9, 'Floor Tom 1 Hit': 11, 'Stick Click': 38, 'Tip Tight': 20, 'Edge Tight': 14, 'Tip Closed': 19,
          'Edge Closed': 13, 'Open 1': 15, 'Open 2': 16, 'Open 3': 17, 'Pedal': 18, 'Pedal Chink': 12, 'CC': 21, 'Ride Bell': 22,
          'Ride Bow': 23, 'China Hit': 31, 'China Choke': 30, 'Main Crash L Hit': 28, 'Main Crash L Choke': 24, 'Wide Crash L Hit': 27,
          'Wide Crash L Choke': 26, 'Main Crash R Hit': 29, 'Splash L Hit': 33, 'Splash L Choke': 32, 'Splash C Hit': 35, 'Splash C Choke': 34,
          'Mini Hats Hit': 36, 'Stack Hit': 37}

halpern_original_nka = {'Kick Main Hit': 2, 'Stick Click Kick Hit': 3, 'Snare Hit': 4, 'Flam': 5, 'Ruff': 6, 'Snare-Off': 7,
                        'Stick Click': 8, 'Hi Tom Hit': 9, 'Hi Tom Rim Hit': 10, 'Mid Tom 1 Main Hit': 11, 'Mid Tom 1 Rim Hit': 12,
                        'Mid Tom 2 Main Hit': 13, 'Mid Tom 2 Rim Hit': 14, 'Floor Tom Main Hit': 15, 'Floor Tom Rim Hit': 16,
                        'Pedal Chik': 17, 'Pedal Ching': 18, 'Tip Tight': 19, 'Edge Tight': 20, 'Tip Closed': 21, 'Edge Closed': 22,
                        'Tip Loose': 23, 'Edge Loose': 24, 'Tip Open 1': 25, 'Edge Open 1': 26, 'Tip Open 2': 27, 'Edge Open 2': 28,
                        'Tip Open 3': 29, 'Edge Open 3': 30, 'Tip Wide': 31, 'Edge Wide': 32, 'Hi Hat CC': 50, 'Left Crash Hit': 33,
                        'Left Crash Bell': 34, 'Left Crash Choke': 35, 'Left Crash Swell': 36, 'Right Crash Hit': 37, 'Right Crash Bell': 38,
                        'Right Crash Choke': 39, 'Right Crash Swell': 40, 'Ride Tip': 41, 'Ride Crash': 42, 'Ride Bell Tip': 43,
                        'Ride Bell Shoulder': 44, 'China Main Hit': 45, 'China Choke': 46, 'Stack Tight Hit': 47, 'Stack Loose Hit': 48,
                        'Splash Hit': 49}



