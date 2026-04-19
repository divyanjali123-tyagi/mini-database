import json
import os

class Database:


    def __init__(self, name):
        self.name     = name
        self.filename = f"{name}.json"
        self.tables   = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tables = json.load(f)
            print(f"Loaded database '{self.name}' from disk")
        else:
            print(f" Created new database '{self.name}'")

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tables, f, indent=2)


    def create_table(self, table_name):
        if table_name in self.tables:
            print(f"Table '{table_name}' already exists")
            return
        self.tables[table_name] = []
        self._save()
        print(f" Table '{table_name}' created")

    def drop_table(self, table_name):
        if table_name not in self.tables:
            print(f" Table '{table_name}' does not exist")
            return
        del self.tables[table_name]
        self._save()
        print(f" Table '{table_name}' dropped")

    def list_tables(self):
        if not self.tables:
            print("No tables found.")
        else:
            print(f"\n Tables in '{self.name}':")
            for t in self.tables:
                print(f"   • {t} ({len(self.tables[t])} rows)")


    def insert(self, table_name, row):
        if table_name not in self.tables:
            print(f" Table '{table_name}' not found")
            return
        row["_id"] = len(self.tables[table_name]) + 1
        self.tables[table_name].append(row)
        self._save()
        print(f"Inserted row with _id={row['_id']} into '{table_name}'")

    def select(self, table_name):
        if table_name not in self.tables:
            print(f" Table '{table_name}' not found")
            return []

        rows = self.tables[table_name]
        if not rows:
            print(f"(no rows in '{table_name}')")
        else:
            print(f"\n '{table_name}' — {len(rows)} rows:")
            for row in rows:
                print(f"   {row}")
        return rows

    def filter(self, table_name, **conditions):
        if table_name not in self.tables:
            print(f" Table '{table_name}' not found")
            return []

        results = []
        for row in self.tables[table_name]:
            match = all(row.get(k) == v for k, v in conditions.items())
            if match:
                results.append(row)

        print(f"\n Filter results ({len(results)} found):")
        for row in results:
            print(f"   {row}")
        return results

    def update(self, table_name, row_id, new_data):
        if table_name not in self.tables:
            print(f" Table '{table_name}' not found")
            return

        for row in self.tables[table_name]:
            if row["_id"] == row_id:
                row.update(new_data)
                self._save()
                print(f" Updated row _id={row_id} in '{table_name}'")
                return

        print(f" Row with _id={row_id} not found")

    def delete(self, table_name, row_id):
        if table_name not in self.tables:
            print(f" Table '{table_name}' not found")
            return

        before = len(self.tables[table_name])
        self.tables[table_name] = [
            r for r in self.tables[table_name] if r["_id"] != row_id
        ]
        after = len(self.tables[table_name])

        if before != after:
            self._save()
            print(f"  Deleted row _id={row_id} from '{table_name}'")
        else:
            print(f" Row with _id={row_id} not found")

    def count(self, table_name):
        if table_name not in self.tables:
            print(f" Table '{table_name}' not found")
            return 0
        total = len(self.tables[table_name])
        print(f" '{table_name}' has {total} rows")
        return total