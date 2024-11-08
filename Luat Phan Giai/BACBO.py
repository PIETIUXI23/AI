def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_queries = int(lines[0])
        queries = []
        for i in range(num_queries):
            query = lines[i + 1].strip()
            queries.append(query)
        num_clauses = int(lines[num_queries + 1])
        clauses = []
        for i in range(num_clauses):
            clause = lines[num_queries + 2 + i].strip()
            clauses.append(clause)
    return queries, clauses

def resolve(clause1, clause2):
    resolved_clause = []
    literals1 = clause1.split(' | ')
    literals2 = clause2.split(' | ')

    complementary_pairs = []
    for literal1 in literals1:
        negated_literal1 = '~' + literal1 if literal1[0] != '~' else literal1[1:]
        if negated_literal1 in literals2:
            complementary_pairs.append((literal1, negated_literal1))

    for literal1 in literals1:
        if literal1 not in [pair[0] for pair in complementary_pairs]:
            resolved_clause.append(literal1)

    for literal2 in literals2:
        if literal2 not in [pair[1] for pair in complementary_pairs]:
            resolved_clause.append(literal2)

    resolved_clause = sorted(set(resolved_clause))

    if resolved_clause:
        resolved_clause = ' | '.join(resolved_clause)
    else:
        resolved_clause = ''

    return resolved_clause

def check_resolvable(clause1, clause2):
    literals1 = clause1.split(' | ')
    literals2 = clause2.split(' | ')
    for literal1 in literals1:
        for literal2 in literals2:
            if literal1 == '~' + literal2 or literal2 == '~' + literal1:
                return True
    return False

def refutation_resolution(queries, clauses):
    knowledge_base = clauses[:]
    resolved_clauses = []
    new_clauses = []
    clause_index = len(clauses) + len(queries) + 1
    with open('output.txt', 'w') as output_file:
        for i, clause in enumerate(clauses, start=1):
            output_file.write(f"{i}.{clause}\n")
        for i, query in enumerate(queries, start=len(clauses) + 1):
            if query.startswith('~'):
                negated_query = query[1:]
            else:
                negated_query = '~' + query
            output_file.write(f"{i}.{negated_query} //phu dinh cua cau can truy van\n")
            knowledge_base.append(negated_query)
        while True:
            found_contradiction = False
            for i in range(len(knowledge_base)):
                for j in range(i + 1, len(knowledge_base)):
                    if check_resolvable(knowledge_base[i], knowledge_base[j]):
                        resolved_clause = resolve(knowledge_base[i], knowledge_base[j])
                        if resolved_clause == '':
                            output_file.write(f"Mau thuan,({i+1}) va ({j+1}) doi lap nhau.\n")
                            output_file.write(f"Tu cau ({i+1}) va ({j+1}) ta nhan duoc cau rong [ ].\n")
                            output_file.write(f"Vay {queries[0]} la he qua logic cua cac cau (1) -- ({len(clauses)}).\n")
                            found_contradiction = True
                            return
                        if resolved_clause not in knowledge_base and resolved_clause not in resolved_clauses:
                            output_file.write(f"{clause_index}.res({i+1},{j+1})=['{resolved_clause}']\n")
                            new_clauses.append((resolved_clause, i+1, j+1))
                            clause_index += 1
                            is_contradiction, contradictory_clauses = check_contradiction(resolved_clause, knowledge_base)
                            if is_contradiction:
                                a = clause_index - 1
                                b = contradictory_clauses[0]
                                output_file.write(f"Mau thuan voi cau {a} va {b} vi res({a},{b})=[ ]\n")
                                output_file.write(f"{queries[0]} la he qua logic cua cac cau (1) -- ({len(clauses)}).\n")
                                return
                if found_contradiction:
                    break
            if found_contradiction:
                break
            if not new_clauses:
                output_file.write(f"{queries[0]} khong la he qua logic cua cac cau (1) -- ({len(clauses)}).\n")
                return False
            resolved_clauses.extend([clause for clause, _, _ in new_clauses])
            knowledge_base.extend([clause for clause, _, _ in new_clauses])
            new_clauses = []

def check_contradiction(new_clause, knowledge_base):
    contradictory_clauses = []
    for i, clause in enumerate(knowledge_base):
        if resolve(new_clause, clause) == '':
            contradictory_clauses.append(i+1)
    if contradictory_clauses:
        return True, contradictory_clauses
    return False, []

def main():
    input_file = 'input.txt'
    queries, clauses = read_input(input_file)
    refutation_resolution(queries, clauses)

if __name__ == "__main__":
    main()