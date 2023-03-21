CREATE TABLE `ShipStaticdata` (
	`id` int NOT NULL,
	`mmsi` int NOT NULL,
	`imo` int NOT NULL,
	`call_sign` varchar(10),
	`name` varchar(120),
	`vessel_type` int,
	`length` FLOAT,
	`width` FLOAT,
	`draught` FLOAT,
	`destination` varchar(50),
	`destination_lon` FLOAT,
	`destination_lat` FLOAT,
	`eta` DATETIME,
	`eta_month` int,
	`eta_day` int,
	`eta_hour` int,
	`eta_minute` int,
	`draught_max` FLOAT,
	`built_year` int,
	`flag` varchar(50),
	`vessel_class` varchar(50),
	`hull_type` varchar(50),
	`engine_type` varchar(50),
	`engine_power` int,
	`deadweight` int,
	`gross_tonnage` int,
	`net_tonnage` int,
	`owner` varchar(50),
	`operator` varchar(50),
	`former_names` varchar(200),
	`place_of_build` varchar(50),
	`yard_number` varchar(50),
	`hull_material` varchar(50),
	`teu_capacity` int,
	`reefers` int,
	`ccs_id` int,
	`ice_class` varchar(50),
	PRIMARY KEY (`id`,`imo`)
);

CREATE TABLE `RouteData` (
	`id` int NOT NULL,
	`destination` varchar(255) NOT NULL,
	`mmsi` int NOT NULL,
	`eta` DATETIME NOT NULL,
	`next_port` varchar(255) NOT NULL,
	`last_port` varchar(255) NOT NULL,
	PRIMARY KEY (`id`,`destination`)
);

CREATE TABLE `CargoData` (
	`id` int NOT NULL,
	`cargo_type` varchar(255) NOT NULL,
	`cargo_weight` FLOAT NOT NULL,
	`cargo_volume` FLOAT NOT NULL,
	`destination` varchar(255) NOT NULL,
	PRIMARY KEY (`id`,`cargo_type`,`destination`)
);

CREATE TABLE `LocationData` (
	`id` int NOT NULL,
	`mmsi` int NOT NULL,
	`location_name` varchar(255) NOT NULL,
	`latitude` FLOAT NOT NULL,
	`longitude` FLOAT NOT NULL,
	PRIMARY KEY (`id`,`location_name`)
);

CREATE TABLE `PositionReport` (
	`id` int NOT NULL,
	`timestamp` DATETIME NOT NULL,
	`mmsi` int NOT NULL,
	`navigational_status` int,
	`rate_of_turn` int,
	`speed_over_ground` FLOAT,
	`position_accuracy` int,
	`longitude` FLOAT NOT NULL,
	`latitude` FLOAT NOT NULL,
	`course_over_ground` FLOAT,
	`true_heading` int,
	`time_of_last_update_sec` int,
	`maneuver_indicator` int,
	`raim_flag` int,
	`communication_state` int,
	PRIMARY KEY (`id`,`timestamp`)
);

ALTER TABLE `RouteData` ADD CONSTRAINT `RouteData_fk0` FOREIGN KEY (`id`) REFERENCES `PositionReport`(`id`);

ALTER TABLE `RouteData` ADD CONSTRAINT `RouteData_fk1` FOREIGN KEY (`eta`) REFERENCES `ShipStaticdata`(`eta`);

ALTER TABLE `CargoData` ADD CONSTRAINT `CargoData_fk0` FOREIGN KEY (`id`) REFERENCES `PositionReport`(`id`);

ALTER TABLE `CargoData` ADD CONSTRAINT `CargoData_fk1` FOREIGN KEY (`destination`) REFERENCES `RouteData`(`destination`);

ALTER TABLE `LocationData` ADD CONSTRAINT `LocationData_fk0` FOREIGN KEY (`id`) REFERENCES `PositionReport`(`id`);

ALTER TABLE `PositionReport` ADD CONSTRAINT `PositionReport_fk0` FOREIGN KEY (`id`) REFERENCES `ShipStaticdata`(`id`);






