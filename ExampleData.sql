USE EXAMPLE

-- Insert data into TableA
INSERT INTO TableA (name)
VALUES 
('Name1'), ('Name2'), ('Name3'), ('Name4'), ('Name5'),
('Name6'), ('Name7'), ('Name8'), ('Name9'), ('Name10'),
('Name11'), ('Name12'), ('Name13'), ('Name14'), ('Name15'),
('Name16'), ('Name17'), ('Name18'), ('Name19'), ('Name20'),
('Name21'), ('Name22'), ('Name23'), ('Name24'), ('Name25'),
('Name26'), ('Name27'), ('Name28'), ('Name29'), ('Name30');

-- Insert data into TableBC and TableCB (1-to-1)
INSERT INTO TableBC (name, id_cb) VALUES ('BCName1', NULL);
INSERT INTO TableCB (name, id_bc) VALUES ('CBName1', SCOPE_IDENTITY());
UPDATE TableBC SET id_cb = 1 WHERE id = 1

-- Insert data into TableDE (1-to-Many parent)
INSERT INTO TableDE (name)
VALUES 
('DEName1'), ('DEName2'), ('DEName3'), ('DEName4'), ('DEName5'),
('DEName6'), ('DEName7'), ('DEName8'), ('DEName9'), ('DEName10'),
('DEName11'), ('DEName12'), ('DEName13'), ('DEName14'), ('DEName15'),
('DEName16'), ('DEName17'), ('DEName18'), ('DEName19'), ('DEName20'),
('DEName21'), ('DEName22'), ('DEName23'), ('DEName24'), ('DEName25'),
('DEName26'), ('DEName27'), ('DEName28'), ('DEName29'), ('DEName30');

-- Insert data into TableEDMany (1-to-Many child)
DECLARE @parentId INT = 1;
WHILE @parentId <= 10
BEGIN
    INSERT INTO TableEDMany (name, id_de)
    VALUES 
        (CONCAT('EDManyName', @parentId, '_1'), @parentId),
        (CONCAT('EDManyName', @parentId, '_2'), @parentId),
        (CONCAT('EDManyName', @parentId, '_3'), @parentId);
    SET @parentId = @parentId + 1;
END;

-- Insert data into TableFGMany (Many-to-Many)
INSERT INTO TableFGMany (name)
VALUES 
('FGName1'), ('FGName2'), ('FGName3'), ('FGName4'), ('FGName5'),
('FGName6'), ('FGName7'), ('FGName8'), ('FGName9'), ('FGName10'),
('FGName11'), ('FGName12'), ('FGName13'), ('FGName14'), ('FGName15'),
('FGName16'), ('FGName17'), ('FGName18'), ('FGName19'), ('FGName20'),
('FGName21'), ('FGName22'), ('FGName23'), ('FGName24'), ('FGName25'),
('FGName26'), ('FGName27'), ('FGName28'), ('FGName29'), ('FGName30');

-- Insert data into TableGFMany (Many-to-Many)
INSERT INTO TableGFMany (name)
VALUES 
('GFName1'), ('GFName2'), ('GFName3'), ('GFName4'), ('GFName5'),
('GFName6'), ('GFName7'), ('GFName8'), ('GFName9'), ('GFName10'),
('GFName11'), ('GFName12'), ('GFName13'), ('GFName14'), ('GFName15'),
('GFName16'), ('GFName17'), ('GFName18'), ('GFName19'), ('GFName20'),
('GFName21'), ('GFName22'), ('GFName23'), ('GFName24'), ('GFName25'),
('GFName26'), ('GFName27'), ('GFName28'), ('GFName29'), ('GFName30');

-- Insert data into PivotFG (Many-to-Many relationship)
DECLARE @fgId INT = 1, @gfId INT = 1;
WHILE @fgId <= 10
BEGIN
    WHILE @gfId <= 10
    BEGIN
        INSERT INTO PivotFG (id_fg, id_gf)
        VALUES (@fgId, @gfId);
        SET @gfId = @gfId + 1;
    END;
    SET @fgId = @fgId + 1;
    SET @gfId = 1;
END;
