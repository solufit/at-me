export interface Task {
	id: string;
	title: string;
	note: string;
	updated: Date;
	selfLink: string;
	parent: string;
	parent_id: string;
	position: string;
	status: string;
	due: Date;
	duringtime: number;
	completed: boolean;
	deleted: boolean;
	hidden: boolean;
	provider: string;
}
