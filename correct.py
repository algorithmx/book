import os, sys, re

eq_reg = re.compile(r"\\\[(\n)?([^\n]*\n?){1,5}\\\]\s*")
eq_inline_reg = re.compile(r"\\\(\s*(?:[^\\]|\\(?!\\\)))*?\s*\\\)")


def correct_euqation_blocks(content0):
    content = str(content0)
    for b in eq_reg.finditer(content0):
        eqn = b.group(0)
        if "\\[\n" in eqn:
            eqn = eqn.replace("\\[\n","$$")
            if "\n\\]" in eqn:
                eqn = eqn.replace("\n\\]","$$\n")
            elif "\\]" in eqn:
                eqn = eqn.replace("\\]","$$\n")
            else:
                raise ValueError(f"Unmatched equation block: {eqn}")
        elif "\\[" in eqn:
            eqn = eqn.replace("\\[","$$")
            if "\n\\]" in eqn:
                eqn = eqn.replace("\n\\]","$$\n")
            elif "\\]" in eqn:
                eqn = eqn.replace("\\]","$$\n")
            else:
                raise ValueError(f"Unmatched equation block: {eqn}")
        else:
            raise ValueError(f"Unmatched equation block: {eqn}")
        content = content.replace(b.group(0), eqn)
    
    content1 = str(content)

    for b in eq_inline_reg.finditer(content1):
        eqn = b.group(0)
        if eqn[:2] == r"\(" and eqn[-2:] == r"\)":
            eqn = "$" + eqn[2:-2].strip() + "$"
            content = content.replace(b.group(0), eqn)
    return content

def main(file):
    content1 = ""
    with open(file, 'r') as f:
        content = f.read()
        content1 = correct_euqation_blocks(content)
    with open(file, 'w') as f:
        f.write(content1)


if __name__ == "__main__":
    # iterate all .md files in current directory
    for file in os.listdir('.'):
        if file.endswith('.md'):
            try:
                main(file)
            except Exception as e:
                print(f"Error processing file {file}: {e}")
                continue
            print(f"Processed file: {file}")
