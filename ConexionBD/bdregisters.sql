CREATE TABLE cities (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255),
status BOOLEAN
);
CREATE TABLE jobsJ(
id int AUTO_INCREMENT PRIMARY KEY,
name varchar(255),
status boolean
);

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    ciudad_id INT,
    job_id INT,
    salary DOUBLE,
    status BOOLEAN DEFAULT 1,
    FOREIGN KEY (ciudad_id) REFERENCES cities(id),
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    ciudad_id INT,
    job_id INT,
    salary DOUBLE,
    status BOOLEAN DEFAULT 1,
    FOREIGN KEY (ciudad_id) REFERENCES cities(id),
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);
