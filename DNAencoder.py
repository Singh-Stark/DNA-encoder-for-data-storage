class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_data_as_string(self):
        current = self.head
        string = ""
        while current:
            string += current.data
            current = current.next
        return string

def text_to_binary(text):
    """Convert text to binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_atgc(binary_str):
    """Convert binary representation to ATGC."""
    atgc_str = ''
    
    for i in range(0, len(binary_str), 2):
        # Get the next two bits
        bits = binary_str[i:i+2]
        if bits == '00':
            atgc_str += 'A'
        elif bits == '01':
            atgc_str += 'T'
        elif bits == '10':
            atgc_str += 'G'
        elif bits == '11':
            atgc_str += 'C'
    
    # If odd length, append '1' (A) or '0' (T)
    if len(binary_str) % 2 != 0:
        # Check the last bit and append accordingly
        last_bit = binary_str[-1]
        if last_bit == '0':
            atgc_str += 'N' 
        else:
            atgc_str += 'U'
    
    return atgc_str

def convert_text_to_atgc_linked_list(text):
    """Convert the input text to its ATGC equivalent, storing in a doubly linked list."""
    binary_str = text_to_binary(text)
    atgc_str = binary_to_atgc(binary_str)
    
    # Create a doubly linked list and insert data in 1KB chunks
    dll = DoublyLinkedList()
    chunk_size = 1024 // 4  # Assuming 4 characters per ATGC pair
    for i in range(0, len(atgc_str), chunk_size):
        chunk = atgc_str[i:i+chunk_size]
        dll.insert_at_end(chunk)
    
    return dll

# Example input text from your document
input_text = """The text is to be pasted here"""

# Convert to ATGC and store in a doubly linked list
dll = convert_text_to_atgc_linked_list(input_text)

# Retrieve the data from the doubly linked list as a string
atgc_output = dll.get_data_as_string()
print("ATGC Equivalent:")
print(atgc_output)