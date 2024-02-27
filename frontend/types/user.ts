interface ProviderInfo {
	id: string;
	photoURL: string;
	displayName: string;
	email: string;
	linkcoede: string;
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
	calenderProvider: string;
	taskProvider: string;
	providers: Providers;
	created_at: Date;
}
