export interface Task {
	id: string;
	title: string;
	note: string;
	updated: Date;
	selfLink: string;
	parent: string;
	position: string;
	status: string;
	due: Date;
	duringtime: number;
	completed: boolean;
	deleted: boolean;
	hidden: boolean;
}
