from docx import Document
import os

# Function to combine Word files and save them as a text file
def combine_word_files(folder_path, output_file):
    # List to store the content of all Word files
    combined_content = []

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx") and not filename.startswith("~$"):
            # Construct the full path of the Word file
            file_path = os.path.join(folder_path, filename)

            # Open the Word document
            doc = Document(file_path)

            # Extract text from each paragraph and add it to the combined_content list
            for paragraph in doc.paragraphs:
                combined_content.append(paragraph.text)

    # Write the combined content to a text file
    output_file_path = os.path.join(folder_path, output_file)
    with open(output_file_path, "w") as f:
        f.write("\n".join(combined_content))

    return output_file_path

# Folder path containing the Word files
folder_path = "C:/Users/Administrator/Desktop/Word File"

# Output file name
output_file = "conversation_transcript.txt"

# Call the function to combine Word files and get the output file path
output_file_path = combine_word_files(folder_path, output_file)

print(f"Conversation transcript saved as '{output_file_path}'")
