import os

folder = r'D:\xdd-skill\docs\Satir family therapy model'

all_files = [
    '01-王剑飞萨提亚家庭治疗课.md',
    '02-原生家庭对个体成长的影响：妈妈角色的影响.md',
    '03-原生家庭对个体成长的影响：父亲角色的重要性.md',
    '04-原生家庭对个人发展的影响与权威关系探讨.md',
    '05-原生家庭对个人发展的影响与亲密关系的探讨.md',
    '06-学员案例案例连线.md',
]

# All teacher name variants → 王老师
teacher_replacements = [
    ('王剑飞', '王老师'),
    ('王建飞', '王老师'),
    ('建飞老师', '王老师'),
    ('剑飞老师', '王老师'),
    ('天飞老师', '王老师'),
    ('金飞老师', '王老师'),
    ('王老师老师', '王老师'),  # fix double 老师
]

# All other replacements
other_replacements = [
    ('丹丹老师', '单单老师'),
    ('兔兔', '工作人员A'),
    ('Alice', '学员A'),
    ('曾逵', '学员B'),
    ('曾魁', '学员B'),
    ('杜超', '学员C'),
]

for fname in all_files:
    fpath = os.path.join(folder, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in teacher_replacements:
        content = content.replace(old, new)
    for old, new in other_replacements:
        content = content.replace(old, new)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Done: {fname}')

print('All 6 files processed.')
