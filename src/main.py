"""
Filename: src.py
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


A GUI application for creating MIDI Note Maps from GetGoodDrums Drum Libraries. The application allows users
to select an input nka file (Kontakt Script Array File) which can be produced by "EXPORT MAP" in Kontakt ,
choose the kit being used and generate a MIDI Note Map based on the selected kit.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from ggd_data import *
from logic import create_reaper_map
import os

class MidiNoteMapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ReaperMidiNoteNameGen-GGD")
        self.root.geometry("500x475")
        self.root.resizable(False, False)

        # UI element variables
        self.input_file_path = ''
        self.output_file_path = ''
        self.kit_selection = ''

        self.checkbox_texts = ["Invasion", "P4 Matt Halpern Kit", "Matt Halpern Signature Pack", "OKW Metal", "OKW Architects", "OKW Aggressive Rock"]
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.border_color = "#34495e"

        self.setup_and_display_ui()

    def setup_and_display_ui(self):
        self.root.configure(bg=self.bg_color)

        style = ttk.Style()
        style.configure('TFrame', bordercolor=self.border_color, relief="solid", borderwidth=2)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.setup_checkboxes()
        self.setup_file_selection_buttons()
        self.setup_run_button()

        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()

    def setup_checkboxes(self):
        self.checkbox_vars = [tk.BooleanVar() for _ in self.checkbox_texts]
        checkbox_frame = ttk.Frame(self.root)
        checkbox_frame.pack(pady=20)

        for i, text in enumerate(self.checkbox_texts):
            chk = ttk.Checkbutton(checkbox_frame, text=text, variable=self.checkbox_vars[i], command=lambda var=self.checkbox_vars[i]: self.update_checkboxes(var))
            chk.grid(row=i, column=0, sticky='w', padx=10, pady=5)

        coming_soon_text = ttk.Label(checkbox_frame, text='More Coming Soon!', foreground=self.fg_color, background=self.bg_color)
        coming_soon_text.grid(row=len(self.checkbox_texts), column=0, pady=10, padx=32)

    def setup_file_selection_buttons(self):
        file_frame = ttk.Frame(self.root)
        file_frame.pack(pady=20)

        input_button = ttk.Button(file_frame, text="Select Input File", command=self.select_input_file)
        self.input_file_label = ttk.Label(file_frame, text="No input file selected", wraplength=400)
        self.input_file_label.grid(row=0, column=1, padx=10, pady=5)
        input_button.grid(row=0, column=0, padx=10, pady=5)

        output_button = ttk.Button(file_frame, text="Select Output File", command=self.select_output_file)
        self.output_file_label = ttk.Label(file_frame, text="No output file selected", wraplength=400)
        self.output_file_label.grid(row=1, column=1, padx=10, pady=5)
        output_button.grid(row=1, column=0, padx=10, pady=5)

    def setup_run_button(self):
        run_button = ttk.Button(self.root, text='Create MIDI Note Map', command=self.run)
        run_button.pack(pady=30)

    def select_input_file(self):
        self.input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("KSP Script Array Files", "*.nka")])
        if self.input_file_path:

            # Display only the file name (full paths get to long)
            self.input_file_label.config(text=os.path.split(self.input_file_path)[-1])

            # Use input filepath to auto-gen an output filepath and update output label
            self.generate_output_filepath_and_label(self.input_file_path)



    def select_output_file(self):
        self.output_file_path = filedialog.asksaveasfilename(title="Select Output File", filetypes=[("Text files", "*.txt")])

        # Making sure that the file ends with '.txt'
        if os.path.splitext(self.output_file_path)[-1] != '.txt':

            self.output_file_path += '.txt'

        # Display only the file name (full paths get to long)
        if self.output_file_path:
            self.output_file_label.config(text=os.path.split(self.output_file_path)[-1])

    def generate_output_filepath_and_label(self, input_filepath):

        # Use input filepath to auto-gen an output filepath and update output label

        input_filepath = os.path.abspath(input_filepath)

        # Replacing nka with txt generates a txt within the same folder as src file
        self.output_file_path = input_filepath.replace('.nka', '.txt')

        # Grab the file name only for displaying to gui
        output_txt = os.path.split(self.output_file_path)[-1]

        # Update gui label
        self.output_file_label.config(text=output_txt)


    def update_checkboxes(self, checked_var):
        for i, var in enumerate(self.checkbox_vars):
            if var != checked_var:
                var.set(False)
            else:
                self.kit_selection = self.checkbox_texts[i]

    def run(self):

        # Making sure necessary gui elements are selected
        if not self.kit_selection:
            messagebox.showwarning("Warning", "Select the kit you are creating a map for!")
            return
        if not self.input_file_path:
            messagebox.showwarning("Warning", "No input file selected!")
            return
        if not self.output_file_path:
            messagebox.showwarning("Warning", "No output file selected!")
            return

        # Execute logic
        try:
            create_reaper_map(self.input_file_path, self.kit_selection, self.output_file_path)
            messagebox.showinfo("Success", "MIDI Note Map Created!")
        except Exception:
            messagebox.showwarning("Failure", "Something went wrong")


if __name__ == '__main__':
    # RUN THE GUI
    root = tk.Tk()
    gui = MidiNoteMapApp(root)
