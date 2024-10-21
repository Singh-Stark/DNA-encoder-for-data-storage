import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, scrolledtext

def atgc_to_binary(atgc_str):
    binary_str = ''
    
    for char in atgc_str:
        if char == 'A':
            binary_str += '00'
        elif char == 'T':
            binary_str += '01'
        elif char == 'G':
            binary_str += '10'
        elif char == 'C':
            binary_str += '11'
    
    # Check if the binary string has an odd length
    if len(binary_str) % 2 != 0:
        # Remove the last two bits added during encoding (assumed to be 'A' or 'T')
        binary_str = binary_str[:-2]  
    
    return binary_str

def binary_to_string(binary_str):
    ascii_chars = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            ascii_chars.append(chr(int(byte, 2)))  # Convert binary byte to ASCII character
    return ''.join(ascii_chars)

def decode_atgc(atgc_str):
    binary_str = atgc_to_binary(atgc_str)
    original_text = binary_to_string(binary_str)
    return original_text

def show_decoded_result(original_text):
    result_window = Toplevel(root)
    result_window.title("Decoded Result")
    result_window.geometry("400x300")

    # Create a scrolled text area to display the results
    text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, font=("Arial", 12), bg='white', fg='black')
    text_area.pack(expand=True, fill='both')

    # Insert decoded data into the text area
    text_area.insert(tk.END, original_text)
    text_area.config(state=tk.NORMAL)  # Make the text area editable to allow copying

def get_atgc_input():
    atgc_str = simpledialog.askstring("Input ATGC", "Enter the ATGC string to decode:")
    if atgc_str:
        try:
            original_text = decode_atgc(atgc_str)
            show_decoded_result(original_text)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decode the ATGC string: {str(e)}")

# Main UI
root = tk.Tk()
root.title("ATGC Decoder")
root.geometry("400x200")

# Button to trigger the ATGC input dialog
decode_button = tk.Button(root, text="Decode ATGC", command=get_atgc_input, font=("Arial", 12))
decode_button.pack(pady=20)

root.mainloop()
