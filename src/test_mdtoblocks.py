from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType
import unittest


class Test(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_blocktype(self):
        type = block_to_block_type("### This is a heading")
        actual_type = BlockType.HEADING
        self.assertEqual(type, actual_type)
    
    def test_block_to_blocktype2(self):
        type = block_to_block_type(
            "- This is a part of an ul\n- This is also part of an ul\n- This too!"
            )
        actual_type = BlockType.UL
        self.assertEqual(type, actual_type)



if __name__ == "__main__":
    unittest.main()
