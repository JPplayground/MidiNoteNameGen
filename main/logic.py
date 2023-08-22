"""
Filename: logic.py
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


This file contains the logic for generating Reaper Midi Note Name files based on a provided nka file
"""

from data import *

def create_reaper_map(input_file, kit_name, output_file):
    # input file == an nka file exported from Kontakt with desired mapping
    # kit name == which GGD library you want a Note Name Text file for
    # output file == desired name of the output text file

    # Reverse the invasion_nka dictionary to map line numbers to kit pieces based on proper kit name
    nka_file_dict : dict
    if kit_name == "Invasion":
        nka_file_dict = {v: k for k, v in invasion_nka.items()}
    elif kit_name == "OKW Metal":
        nka_file_dict = {v: k for k, v in metal_nka.items()}
    elif kit_name == "OKW Architects":
        nka_file_dict = {v: k for k, v in architects_nka.items()}
    elif kit_name == "OKW Aggressive Rock":
        nka_file_dict = {v: k for k, v in aggressive_rock_nka.items()}
    elif kit_name == "P4 Matt Halpern Kit":
        nka_file_dict = {v: k for k, v in p4_nka.items()}
    elif kit_name == "Matt Halpern Signature Pack":
        nka_file_dict = {v: k for k, v in halpern_original_nka.items()}
    else:
        print("Invalid Kit Name")
        print(kit_name)
        return

    with open(input_file, 'r') as f:

        used_note_numbers = []
        num_and_kit_piece = []

        set_of_lines = f.read().splitlines()

        for line_number, kontakt_midi_note_number in enumerate(set_of_lines):

            # line 0 is always '%ART__articulation_map', or non-used line number
            if line_number == 0 or int(kontakt_midi_note_number) < 0:
                continue

            append_me = ''

            # GET REAPER MIDI NOTE NUMBER
            # ================================================ #
            # get string to use as dictionary key lookup
            kontakt_midi_string = KONTAKT_NOTES[int(kontakt_midi_note_number)]
            # convert from kontakt note to reaper note
            reaper_note = convert_kontakt_note_to_reaper_note(kontakt_midi_string)
            # get the index of that reaper note
            reaper_note_number = str(get_number_from_note(reaper_note))
            # add to string
            append_me += reaper_note_number
            # track used note numbers (to fill in unused numbers with '~'
            used_note_numbers.append(int(reaper_note_number))
            # ================================================ #

            # GET KIT PIECE NAME
            # ================================================ #
            if line_number in nka_file_dict.keys():
                kit_piece = nka_file_dict[line_number]
                append_me += ' ' + kit_piece
            # ================================================ #

            # APPEND (reaper_note_number kit_piece)
            num_and_kit_piece.append(append_me)

    # FILL IN REMAINING UNUSED REAPER NOTES
    # ================================================ #
    # using our tracked un-used note numbers, and knowing the size of associated nka files
    for i in range(128):
        if i not in used_note_numbers:
            append_me = f'{i} ~'
            num_and_kit_piece.append(append_me)

    with open(output_file, 'w') as f:
        for line in num_and_kit_piece:
            f.write(line)
            f.write('\n')




