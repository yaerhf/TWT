import json
import os

"""
TWT Dataset Builder: Mono-covalent bond empirical empirical data
We include integer quantum data but strictly prohibit empirical constants 
(like Slater's Z_eff or Pauling Electronegativity) to ensure the neural 
engine discovers continuous physics equations completely blindly.
"""

# Atom Dictionary: [Z (protons), N (neutrons approx), n (shell index), v (valence electrons)]
atoms = {
    'H':  {'Z': 1,  'N': 0,   'n': 1, 'v': 1},
    'F':  {'Z': 9,  'N': 10,  'n': 2, 'v': 7},
    'Cl': {'Z': 17, 'N': 18,  'n': 3, 'v': 7},
    'Br': {'Z': 35, 'N': 45,  'n': 4, 'v': 7},
    'I':  {'Z': 53, 'N': 74,  'n': 5, 'v': 7}
}

# Bond Library in Angstroms
bonds_data = [
    # Symmetrical
    ('H', 'H', 0.74),
    ('F', 'F', 1.42),
    ('Cl', 'Cl', 1.99),
    ('Br', 'Br', 2.28),
    ('I', 'I', 2.67),
    
    # Asymmetrical (Validation potential)
    ('H', 'F', 0.92),
    ('H', 'Cl', 1.27),
    ('H', 'Br', 1.41),
    ('H', 'I', 1.61),
    ('Cl', 'F', 1.63),
    ('Br', 'Cl', 2.14),
    ('I', 'Br', 2.47),
    ('I', 'Cl', 2.32)
]

def compile_dataset():
    test_set_keys = [('H', 'Cl'), ('Br', 'Br'), ('I', 'Br')]
    
    training_data = []
    testing_data = []
    
    for atom_A, atom_B, length in bonds_data:
        data_point = {
            'atom_A': atoms[atom_A],
            'atom_B': atoms[atom_B],
            'empirical_3D_length': length
        }
        
        if (atom_A, atom_B) in test_set_keys:
            testing_data.append(data_point)
        else:
            training_data.append(data_point)
            
    dataset = {
        'training': training_data,
        'testing': testing_data
    }
    
    output_path = os.path.join(os.path.dirname(__file__), 'covalent_dataset.json')
    with open(output_path, 'w') as f:
        json.dump(dataset, f, indent=4)
        
    print(f"[{len(training_data)} Training targets, {len(testing_data)} Validation targets] compiled successfully.")
    
if __name__ == '__main__':
    compile_dataset()
