class Rule:
    @staticmethod
    def run(cell):
        if cell.organism.is_alive:
            if cell.organism.number_neighbors != 2 and cell.organism.number_neighbors != 3:
                cell.organism.kill()
        else:
            if cell.organism.number_neighbors == 3:
                cell.organism.resurrect()