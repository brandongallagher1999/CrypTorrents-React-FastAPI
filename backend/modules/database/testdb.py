import sqlite3




def main():

    connection = sqlite3.connect("db.db")
    c = connection.cursor()


    # User login model to be stored in database

    # c.execute('''
    #     CREATE TABLE IF NOT EXISTS `user_login` (
    #         `id` INT AUTO_INCREMENT NOT NULL,
    #         `username` VARCHAR(45) NOT NULL,
    #         `password` VARCHAR(100) NULL,
    #     PRIMARY KEY (`id`));
    # ''')

    
    #Creating the user table related to what the model wants to see --> for later relationship join
    
    # c.execute('''
    #         CREATE TABLE IF NOT EXISTS `user` (
    #             `username` VARCHAR(25) NOT NULL,
    #             `id` INT NOT NULL,
    #             `logged_in` BIT NOT NULL DEFAULT 0,
    #         PRIMARY KEY (`id`),
    #         CONSTRAINT `id`
    #         FOREIGN KEY (`id`)
    #         REFERENCES `user_login` (`id`)
    #         ON DELETE NO ACTION
    #         ON UPDATE NO ACTION);
    # ''')


    #Creating the torrent table

    # c.execute('''

    #     CREATE TABLE IF NOT EXISTS `torrent` (
    #         `name` VARCHAR(100) NOT NULL,
    #         `magnet` VARCHAR(255) NOT NULL,
    #         `size` VARCHAR(45) NOT NULL DEFAULT 0,
    #         `category` VARCHAR(45) NOT NULL,
    #         `user_id` INT NOT NULL,
    #     CONSTRAINT `user_id`
    #     FOREIGN KEY (`user_id`)
    #     REFERENCES `user` (`id`)
    #     ON DELETE NO ACTION
    #     ON UPDATE NO ACTION);
    # ''')

    c.execute('''

    INSERT INTO 'torrent' VALUES
    (
        'name',
        'magnet',
        'size',
        'category',
        1
    );
    '''
    )
    connection.commit()

    for row in c.execute("SELECT * FROM `torrent`;"):
        print(row)






    connection.close()

main()
    

    