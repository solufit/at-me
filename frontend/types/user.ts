interface ProviderInfo {
	id: string;
	photoURL: string;
	displayName: string;
	email: string;
}

interface Providers {
	atme: ProviderInfo;
	google: ProviderInfo;
	github: ProviderInfo;
}

export interface User {
	userId: string;
	displayName: string;
	email: string;
	photoURL: string;
	calendarProvider: string;
	taskProvider: string;
	providers: Providers;
	loginProvider: string;
	created_at: Date;
}
