def addDogs(con ,name, description, link):
    try:
        con.execute(f"""insert into Dogs(name, description, link)
                    values ('{name}','{description}','{link}')""")

        con.commit()
        return True
    except:
        return False

def readDogs(con):
    data = con.execute("select * from Dogs;")
    return data.fetchall()





