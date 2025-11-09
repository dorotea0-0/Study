def sort_roles(roles, textLines):
    role_dict = {role: [] for role in roles}
    sorted_roles_by_length = sorted(roles, key=len, reverse=True)
    current_role = None
    current_replique_lines = []
    current_replique_start_line_num = None
    for i, line in enumerate(textLines):
        found_role = False
        for role in sorted_roles_by_length:
            if line.startswith(f"{role}:"):
                if current_role is not None and current_replique_lines:
                    full_text = "\n".join(current_replique_lines)
                    role_dict[current_role].append(f"{current_replique_start_line_num}) {full_text}")
                current_role = role
                text = line[len(role) + 1:].lstrip()
                current_replique_lines = [text] if text else []
                current_replique_start_line_num = i + 1
                found_role = True
                break
        if not found_role and current_role is not None:
            current_replique_lines.append(line)
    if current_role is not None and current_replique_lines:
        full_text = "\n".join(current_replique_lines)
        role_dict[current_role].append(f"{current_replique_start_line_num}) {full_text}")
    result = []
    for role in roles:
        result.append(f"{role}:")
        for replique in role_dict[role]:
            result.append(replique)
        result.append("")
    if result:
        result.pop()
    return "\n".join(result)
with open("roles.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()
roles_start = lines.index("roles:")
text_start = lines.index("textLines:")
roles = lines[roles_start + 1 : text_start]
textLines = lines[text_start + 1 :]
output = sort_roles(roles, textLines)
print(output)